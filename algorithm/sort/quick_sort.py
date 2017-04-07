#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2017-03-19 23:35:44
# @Author  : Yummy (lookyummy@163.com)
# @Link    : https://github.com/whyallwaysme
# @Version : $Id$

'''
原理
快速排序使用分治法（Divide and conquer）策略来把一个序列（list）分为两个子序列（sub-lists）。

步骤
1.从数列中挑出一个元素，称为"基准"（pivot），
2.重新排序数列，所有元素比基准值小的摆放在基准前面，所有元素比基准值大的摆在基准的后面（相同的数可以到任一边）。
  在这个分区结束之后，该基准就处于数列的中间位置。这个称为分区（partition）操作。
3.递归地（recursive）把小于基准值元素的子数列和大于基准值元素的子数列排序。
'''

# 普通版
def quick_sort(sort_list):
    less = []
    pivotList = []
    more = []
    # 递归出口
    if len(sort_list) <= 1:
        return sort_list
    else:
        # 将第一个值做为基准
        pivot = sort_list[0]
        for i in sort_list:
            # 将比基准小的值放到less数列
            if i < pivot:
                less.append(i)
            # 将比基准大的值放到more数列
            elif i > pivot:
                more.append(i)
            # 将和基准相同的值保存在基准数列
            else:
                pivotList.append(i)
        # 对less数列和more数列继续进行排序
        less = quick_sort(less)
        more = quick_sort(more)
        return less + pivotList + more


def my_quick_sort(sort_list):
    less = []
    guard_list = []
    more = []

    if len(sort_list) <= 1:
        return sort_list
    else:
        guard = sort_list[0]

        for x in sort_list:

            if x > guard:
                more.append(x)
            elif x < guard:
                less.append(x)
            else:
                guard_list.append(x)

        less = my_quick_sort(less)
        more = my_quick_sort(more)

        return less + guard_list + more

# python cookbook三行实现python快速排序
def qsort(arr):
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[0]
        return qsort([x for x in arr[1:] if x < pivot]) + \
               [pivot] + \
               qsort([x for x in arr[1:] if x >= pivot])


if __name__ == '__main__':
    A = [5,-4,6,3,7,11,1,2]
    print 'Before sort:', A
    A = quick_sort(A)
    print 'After sort:', A