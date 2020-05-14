# 算法-动态规划

Those who cannot remember the past are condemned to repeat it.

## 它是什么?

### Dynamic programming，简称DP。通过把原问题分解为相对简单的子问题的方式求解复杂问题的方法。

### 核心

- 记住已经求过的子问题的解

## 例子

### 经典问题

- 爬楼梯问题
- 01背包问题

	- 问题描述，给定一组n个物品，每种物品都有自己的重量w和价值v，在限定的总重量/总容量内，选择其中若干个（也即每种物品可以选0个或1个），设计选择方案使得物品的总价值最高
	- 思考:其他方式不可以么？比如，性价比计算，只拿贵的？答案，不行，只拿按照单个物品性价比高的情况下怎么使空间全部占满？所以总体计算下来单个性价比最高不一定等于总体性价比最高

### 做过的算法题目

- 解码方法问题

  https://github.com/jankin3/project-leetcode/blob/master/91-Decode-Ways-analysis.md

- 分词问题

  https://github.com/jankin3/project-leetcode/blob/master/139-wordbreak-analysis.md

- 最佳买卖股票时机含冷冻期 问题

  https://github.com/jankin3/project-leetcode/blob/master/309-best-time-to-buy-and-sell-stock-with-cooldown-analysis.md

## 它有什么？

### 两个要素

- 状态转移方程
- 临界条件

## 使用

### 场景

- 重叠子问题和最优子结构

### 方法

- 表格

	- 目的就是去不断推导，完成状态转移， 表格中的每一个cell都是一个小问题， 我们先解决规模为寻常的情况，然后根据这个结果逐步推导

## 关联算法

### 递归

参考:https://github.com/azl397985856/leetcode/blob/master/thinkings/dynamic-programming.md

- 对比

	- 递归，从问题的结果倒推，直到问题的规模缩小到寻常。
	- 动态规划，就是从寻常入手， 逐步扩大规模到最优子结构

### 贪婪算法

- to do

*XMind: ZEN - Trial Version*