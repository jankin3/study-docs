# 　-*- coding: utf-8 -*-
# 堆排序

def heap_sort(nums):
    n_len = len(nums)

    for i in range(n_len - 1, -1, -1): # heapify init
        heapify(nums, i, n_len - 1)

    for j in range(n_len): # place one and heapify again
        nums[0], nums[n_len - 1 - j] = nums[n_len - 1 - j], nums[0]
        heapify(nums, 0, n_len - 2 - j)


def heapify(nums, start, n):
    '''
    change to heap
    :param nums: 数组
    :param start: 开始位置
    :param n: 总长度
    :return: Ｎｏｎｅ
    '''
    l = 2 * start + 1  # 左孩子
    r = l + 1  # 右孩子
    if l > n or r > n:
        return

        # find largest and swap
    largest = start
    if nums[l] > nums[largest]:
        largest = l
    if nums[r] > nums[largest]:
        largest = r
    if largest != start:
        nums[start], nums[largest] = nums[largest], nums[start]
        heapify(nums, largest, n)  # continue


nums = [1, 3, 6, 7, 2, 4]
heap_sort(nums)
print('Result: %s' % nums)
