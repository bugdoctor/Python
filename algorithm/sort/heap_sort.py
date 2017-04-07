#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2017-03-19 23:29:57
# @Author  : Yummy (lookyummy@163.com)
# @Link    : https://github.com/whyallwaysme
# @Version : $Id$

'''
原理
堆排序（Heapsort）是指利用堆这种数据结构所设计的一种排序算法。堆积是一个近似完全二叉树的结构，并同时满足堆积的性质：即子结点的键值或索引总是小于（或者大于）它的父节点。

步骤
1.创建最大堆:将堆所有数据重新排序，使其成为最大堆
2.最大堆调整:作用是保持最大堆的性质，是创建最大堆的核心子程序
3.堆排序:移除位在第一个数据的根节点，并做最大堆调整的递归运算
'''

#最大堆调整：将堆的末端子节点作调整，使得子节点永远小于父节点
#start为当前需要调整最大堆的位置，end为调整边界
def sift_down(arr, start, end):
    root = start
    while True:
        # 从root开始对最大堆调整
        child = 2 * root + 1                #调整节点的子节点，即左孩子
        '''
        为什么左孩纸是2*root+1而不是2*root
        原因：因为数组下标是从0开始，所以需要+1
        '''
        if child > end: # 调整完毕
            break

        # 找出两个child中较大的一个
        if child + 1 <= end and arr[child] < arr[child + 1]:
            child += 1             #取较大的子节点

        if arr[root] < arr[child]:     #较大的子节点成为父节点
            # 最大堆小于较大的child, 交换顺序
            arr[root], arr[child] = arr[child], arr[root]

            # 正在调整的节点设置为root
            root = child
        else:
            # 无需调整的时候, 退出
            break


def heap_sort(arr):
    # 从最后一个有子节点的孩子开始调整最大堆,最后一个有子节点的孩子 = int(length)/2 因为数组下标从0开始，所以-1
    first = len(arr) / 2 - 1       #最后一个非叶子节点
    for start in range(first, -1, -1):     #构造大根堆
        sift_down(arr, start, len(arr) - 1)
    print 'arr first sift:   ', arr
    # 将最大的放到堆的最后一个, 堆-1, 继续调整排序
    for end in range(len(arr) - 1, 0, -1):           #堆排，将大根堆转换成有序数组
        arr[0], arr[end] = arr[end], arr[0]
        print 'arr before sift:   ', arr
        sift_down(arr, 0, end - 1)
        print 'arr has sifted:   ', arr

    return arr

if __name__ == '__main__' :

    A = [10, -3, 5, 7, 1, 3, 7]
    print 'Before sort:', A
    A = heap_sort(A)
    print 'After sort:', A