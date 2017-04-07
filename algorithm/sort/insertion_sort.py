#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2017-03-19 23:23:47
# @Author  : Yummy (lookyummy@163.com)
# @Link    : https://github.com/whyallwaysme
# @Version : $Id$

'''
原理
插入排序（Insertion Sort）是一种简单直观的排序算法。它的工作原理是通过构建有序序列，对于未排序数据，在已排序序列中从后向前扫描，找到相应位置并插入。

步骤
1.从第一个元素开始，该元素可以认为已经被排序
2.取出下一个元素，在已经排序的元素序列中从后向前扫描
3. 如果该元素（已排序）大于新元素，将该元素移到下一位置
4.重复步骤3，直到找到已排序的元素小于或者等于新元素的位置
5.将新元素插入到该位置后
6.重复步骤2~5
'''

# 稳定，时间复杂度 O(n^2)
def insert_sort(sort_list):
    n = len(sort_list)
    for i in range(1, n):
        # 后一个元素和前一个元素比较
        # 如果比前一个小
        if sort_list[i] < sort_list[i - 1]:
            # 将这个数取出
            temp = sort_list[i] # 比较参考值
            # 保存下标
            index = i
            # 从后往前依次比较每个元素
            for j in range(i - 1, -1, -1): #从i-1 循环到 0 (包括0)

                if sort_list[j] > temp: # 将所有比temp大的数移动到它的右边
                    sort_list[j + 1] = sort_list[j]
                    index = j # 记录空出来的下标
                else:
                    break
            # 插入元素
            sort_list[index] = temp
    return sort_list

def my_insert_sort(sort_list):
    length = len(sort_list)

    for i in xrange(1, length):

        if sort_list[i] < sort_list[i - 1]:
            index = i
            guard = sort_list[i]

            for j in range(i-1, -1, -1):

                if sort_list[j] > guard:
                    sort_list[j + 1] = sort_list[j]
                    index = j
                else:
                    break

            sort_list[index] = guard

    return sort_list

if __name__ == '__main__':
    nums = [10,8,4,-1,2,6,7,3]
    print 'nums is:', nums
    nums = insert_sort(nums)
    print 'insert sort:', nums