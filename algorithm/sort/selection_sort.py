#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2017-03-19 23:27:22
# @Author  : Yummy (lookyummy@163.com)
# @Link    : https://github.com/whyallwaysme
# @Version : $Id$

'''
选择排序(Selection sort)是一种简单直观的排序算法。它的工作原理如下。首先在未排序序列中找到最小（大）元素，存放到

排序序列的起始位置，然后，再从剩余未排序元素中继续寻找最小（大）元素，然后放到已排序序列的末尾。以此类推，直到所

有元素均排序完毕。

步骤
1.在未排序序列中找到最小（大）元素，存放到排序序列的起始位置，
2.再从剩余未排序元素中继续寻找最小（大）元素，然后放到已排序序列的末尾。
3.重复第二步，直到所有元素均排序完毕。
'''

# 不稳定，时间复杂度 O(n^2)

# 核心：找到一次循环比较排序中最小的值，放到开始位，然后开始下一次循环比较排序
def select_sort(sort_list):
    ''''' 选择排序
    每一趟从待排序的数据元素中选出最小（或最大）的一个元素，
    顺序放在已排好序的数列的最后，直到全部待排序的数据元素排完。
    选择排序是不稳定的排序方法。
    '''
    length = len(sort_list)
    # 在0-n-1上依次选择相应大小的元素
    for i in xrange(length):
        min_index = i # 记录最小元素的下标
        # 查找最小值
        for j in xrange(i + 1, length):
            if sort_list[j] < sort_list[min_index]:
                min_index = j
        #找到最小元素进行交换
        if min_index != i:
            sort_list[i], sort_list[min_index] = sort_list[min_index], sort_list[i]

    return sort_list

if __name__ == '__main__':
    A = [10, -3, 5, 7, 1, 3, 7]
    print 'Before sort:',A
    a = select_sort(A)
    print 'After sort:',A
