#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2017-03-20 15:47:53
# @Author  : Yummy (lookyummy@163.com)
# @Link    : https://github.com/whyallwaysme
# @Version : $Id$

'''
原理

冒泡排序(Bubble Sort)是一种简单的排序算法。它重复地走访过要排序的数列，一次比较两个元素，
如果他们的顺序错误就把他们交换过来。走访数列的工作是重复地进行直到没有再需要交换，也就是说该数列已经排序完成。这个算法的名字由来是因为越小的元素会经由交换慢慢“浮”到数列的顶端。

步骤

冒泡排序算法的运作如下：

1.比较相邻的元素。如果第一个比第二个大，就交换他们两个。
2.对每一对相邻元素作同样的工作，从开始第一对到结尾的最后一对。这步做完后，最后的元素会是最大的数。
3.针对所有的元素重复以上的步骤，除了最后一个。
4.持续每次对越来越少的元素重复上面的步骤，直到没有任何一对数字需要比较。
'''

# 最简单冒泡
def simple_bubble_sort(sort_list):
    length = len(sort_list)
    # 第一级遍历
    for i in range(length):
        # 第二级遍历
        for j in range(i, length):
            # 交换两者数据，这里没用temp是因为python 特性元组。
            if sort_list[i] > sort_list[j]:
                sort_list[i], sort_list[j] = sort_list[j], sort_list[i]

    return sort_list

# 正宗倒序冒泡排序
def bubble_sort(sort_list):
    length = len(sort_list)

    for i in range(length):
        # range从length开始是因为j = length - 1是循环起点，sort_list最后一位是sort_list[length - 1] 而不是sort_list[length]
        for j in range(length-1, i, -1):
            if sort_list[j] < sort_list[j - 1]:
                sort_list[j], sort_list[j - 1] = sort_list[j - 1], sort_list[j]

    return sort_list

# 这种排序其实还可以稍微优化一下，添加一个标记，在排序已完成时，停止排序。
def flag_bubble_sort(sort_list):
    length = len(sort_list)

    for i in range(length):
        # 标志位
        flag = True
        for j in range(i, length):

            if sort_list[i] > sort_list[j]:
                sort_list[i], sort_list[j] = sort_list[j], sort_list[i]
                flag = False
        # 没有发生交换，直接返回sort_list
        if flag:
            return sort_list

    return sort_list


if __name__ == '__main__':
    A = [10, -3, 5, 7, 1, 3, 7]
    print 'Before sort:',A
    A = bubble_sort(A)
    print 'After sort:', A