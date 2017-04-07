#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2017-03-19 23:28:42
# @Author  : Yummy (lookyummy@163.com)
# @Link    : https://github.com/whyallwaysme
# @Version : $Id$

'''
希尔排序，也称递减增量排序算法,希尔排序是非稳定排序算法。该方法又称缩小增量排序，因DL．Shell于1959年提出而得名。

先取一个小于n的整数d1作为第一个增量，把文件的全部记录分成d1个组。所有距离为d1的倍数的记录放在同一个组中。先在各组内进行排序；

然后，取第二个增量d2

步骤
每次以一定步长(就是跳过等距的数)进行排序，直至步长为1.
'''

# 不稳定，时间复杂度 平均时间 O(nlogn) 最差时间O(n^s)1
def shell_sort(sort_list):
    # 希尔排序
    n = len(sort_list)
    gap = int(round(n/2))       #初始步长 , 用round四舍五入取整

    while gap > 0 :

        for i in range(gap, n):        #每一列进行插入排序 , 从gap 到 n-1
            temp = sort_list[i]
            j = i

            while ( j >= gap and sort_list[j - gap] > temp ):    #插入排序
                sort_list[j] = sort_list[j - gap]
                j = j - gap

            sort_list[j] = temp

        gap = int(round(gap/2))                     #重新设置步长

    return sort_list

if __name__ == '__main__':
    A = [10, -3, 5, 7, 1, 3, 7]
    print 'Before sort:',A
    A = shell_sort(A)
    print 'After sort:', A
