#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2017-03-19 23:16:30
# @Author  : Yummy (lookyummy@163.com)
# @Link    : https://github.com/whyallwaysme
# @Version : $Id$

'''
归并排序

归并排序也称合并排序，是分治法的典型应用。分治思想是将每个问题分解成个个小问题，将每个小问题解决，然后合并。

具体的归并排序就是，将一组无序数按n/2递归分解成只有一个元素的子项，一个元素就是已经排好序的了。然后将这些有序的子元素进行合并。

合并的过程就是对两个已经排好序的子序列，先选取两个子序列中最小的元素进行比较，选取两个元素中最小的那个子序列并将其从子序列中

去掉添加到最终的结果集中，直到两个子序列归并完成。

递归法

假设序列共有n个元素：

1.将序列每相邻两个数字进行归并操作，形成 {displaystyle floor(n/2)} floor(n/2)个序列，排序后每个序列包含两个元素
2.将上述序列再次归并，形成 {displaystyle floor(n/4)} floor(n/4)个序列，每个序列包含四个元素
3.重复步骤2，直到所有元素排序完毕
'''

# 稳定，时间复杂度  O(nlog n)
# 递归法
def merge_sort(sort_list):
    # 认为长度不大于1的数列是有序的
    if len(sort_list) <= 1:
        return sort_list
    # 二分列表
    middle = len(sort_list) / 2

    left = merge_sort(sort_list[:middle])
    right = merge_sort(sort_list[middle:])
    # 最后一次合并
    return merge(left, right)

# 合并
def merge(left, right):
    i, j = 0, 0
    result = []
    while i < len(left) and j < len(right):
        # 找出较小值,放入结果序列中
        if left[i] <= right[j]: # 左边的数小
            result.append(left[i])
            i += 1
        else: # 右边的数小
            result.append(right[j])
            j += 1

    # 左边或者右边一定会有剩下的数，直接连接到队列结尾
    result += left[i:]
    result += right[j:]

    return result


if __name__ == '__main__':
    nums = [10,8,4,-1,2,6,7,3, 9]
    print 'nums is:', nums
    nums = merge_sort(nums)
    print 'merge sort:', nums
