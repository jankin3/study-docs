class Solution():
    def merge_sort(self, nums):
        if len(nums) == 1:
            return nums
        else:
            mid_index = len(nums) / 2
            left = self.merge_sort(nums[:mid_index])
            right = self.merge_sort(nums[mid_index:])
            return self.merge(left, right)


    def merge(self, left, right):
        '''
        merge list
        :param left: list 1
        :param right: list 2
        :return: merged list
        '''
        i, j = 0, 0
        c = []
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                c.append(left[i])
                i += 1
            else:
                c.append(right[j])
                j += 1
        if i < len(left):
            c = c + left[i:]
        if j < len(right):
            c = c + right[j:]
        return c

s = Solution()
r = s.merge_sort([5,3,0,6,1,4])
print('result:')
print(r)