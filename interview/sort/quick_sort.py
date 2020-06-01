# 快速排序
def quick_sort(nums, l, r):
    if l < r:
        index = partion(nums, l, r)
        quick_sort(nums, l, index - 1)
        quick_sort(nums, index + 1, r)


def partion(nums, l, r):
    x = nums[l]
    index = l  # 指向最后一个小于x的位置
    for j in range(l + 1, r + 1):
        if nums[j] < x:
            index += 1
            nums[j], nums[index] = nums[index], nums[j]
    nums[index], nums[l] = nums[l], nums[index]
    return index


nums = [1, 3, 6, 7, 2, 4]
quick_sort(nums, 0, 5)
print(nums)
