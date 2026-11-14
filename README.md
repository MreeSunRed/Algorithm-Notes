# Algorithm-Notes

个人算法刷题笔记 —— 记录每道题的**思路推导**、**复杂度分析**、**易错点**与**可运行代码**。

> 目标不是「抄一份 AC 代码」，而是留下「下次遇到同类题能想起怎么下手」的线索。

## 题目索引

| # | 题目 | 难度 | 核心考点 | 笔记 | 代码 |
|---|------|:----:|----------|:----:|:----:|
| 1 | [两数之和](https://leetcode.cn/problems/two-sum/) | 简单 | 哈希表 · 空间换时间 | [📝](notes/01-两数之和.md) | [🐍](solutions/两数之和.py) |
| 2 | [最大子数组和](https://leetcode.cn/problems/maximum-subarray/) | 中等 | 动态规划 · Kadane 算法 | [📝](notes/02-最大子数组和.md) | [🐍](solutions/最大子数组和.py) |
| 3 | [相交链表](https://leetcode.cn/problems/intersection-of-two-linked-lists/) | 简单 | 链表 · 哈希集合 / 双指针 | [📝](notes/03-相交链表.md) | [🐍](solutions/相交链表.py) |
| 4 | [有效的括号](https://leetcode.cn/problems/valid-parentheses/) | 简单 | 字符串 · 栈 | [📝](notes/04-有效的括号.md) | [🐍](solutions/有效的括号.py) |
| 5 | [买卖股票的最佳时机](https://leetcode.cn/problems/best-time-to-buy-and-sell-stock/) | 简单 | 数组 · 动态规划 | [📝](notes/05-买卖股票的最佳时机.md) | [🐍](solutions/买卖股票的最佳时机.py) |
| 6 | [二叉树的中序遍历](https://leetcode.cn/problems/binary-tree-inorder-traversal/) | 简单 | 树 · 递归 / 显式栈 | [📝](notes/06-二叉树的中序遍历.md) | [🐍](solutions/二叉树的中序遍历.py) |
| 7 | [二叉树的最大深度](https://leetcode.cn/problems/maximum-depth-of-binary-tree/) | 简单 | 树 · DFS / BFS | [📝](notes/07-二叉树的最大深度.md) | [🐍](solutions/二叉树的最大深度.py) |
| 8 | [合并区间](https://leetcode.cn/problems/merge-intervals/) | 中等 | 数组 · 排序 | [📝](notes/08-合并区间.md) | [🐍](solutions/合并区间.py) |
| 9 | [反转链表](https://leetcode.cn/problems/reverse-linked-list/) | 简单 | 链表 · 双指针 / 递归 | [📝](notes/09-反转链表.md) | [🐍](solutions/反转链表.py) |
| 10 | [回文链表](https://leetcode.cn/problems/palindrome-linked-list/) | 简单 | 链表 · 快慢指针 / 反转 | [📝](notes/10-回文链表.md) | [🐍](solutions/回文链表.py) |
| 11 | [字符串解码](https://leetcode.cn/problems/decode-string/) | 中等 | 字符串 · 栈 / 递归 | [📝](notes/11-字符串解码.md) | [🐍](solutions/字符串解码.py) |
| 12 | [反转二叉树](https://leetcode.cn/problems/invert-binary-tree/) | 简单 | 树 · 递归 / BFS | [📝](notes/12-反转二叉树.md) | [🐍](solutions/反转二叉树.py) |
| 13 | [对称二叉树](https://leetcode.cn/problems/symmetric-tree/) | 简单 | 树 · 递归 / 镜像比较 | [📝](notes/13-对称二叉树.md) | [🐍](solutions/对称二叉树.py) |
| 14 | [轮转数组](https://leetcode.cn/problems/rotate-array/) | 中等 | 数组 · 反转 / 原地操作 | [📝](notes/14-轮转数组.md) | [🐍](solutions/轮转数组.py) |
| 15 | [字母异位词分组](https://leetcode.cn/problems/group-anagrams/) | 中等 | 字符串 · 哈希表 / 排序 | [📝](notes/15-字母异位词分组.md) | [🐍](solutions/字母异位词分组.py) |
| 16 | [环形链表](https://leetcode.cn/problems/linked-list-cycle/) | 简单 | 链表 · 哈希表 / 快慢指针 | [📝](notes/16-环形链表.md) | [🐍](solutions/环形链表.py) |
| 17 | [最小栈](https://leetcode.cn/problems/min-stack/) | 中等 | 栈 · 设计 / 辅助栈 | [📝](notes/17-最小栈.md) | [🐍](solutions/最小栈.py) |
| 18 | [二叉树的直径](https://leetcode.cn/problems/diameter-of-binary-tree/) | 简单 | 树 · 后序遍历 | [📝](notes/18-二叉树的直径.md) | [🐍](solutions/二叉树的直径.py) |
| 19 | [将有序数组转换为二叉搜索树](https://leetcode.cn/problems/convert-sorted-array-to-binary-search-tree/) | 简单 | 树 · 分治 / 二叉搜索树 | [📝](notes/19-将有序数组转换为二叉搜索树.md) | [🐍](solutions/将有序数组转换为二叉搜索树.py) |
| 20 | [无重复字符的最长子串](https://leetcode.cn/problems/longest-substring-without-repeating-characters/) | 中等 | 字符串 · 滑动窗口 / 哈希表 | [📝](notes/20-无重复字符的最长子串.md) | [🐍](solutions/无重复字符的最长子串.py) |
| 21 | [除了自身以外数组的乘积](https://leetcode.cn/problems/product-of-array-except-self/) | 中等 | 数组 · 前缀积 / 后缀积 | [📝](notes/21-除了自身以外数组的乘积.md) | [🐍](solutions/除了自身以外数组的乘积.py) |
| 22 | [环形链表 II](https://leetcode.cn/problems/linked-list-cycle-ii/) | 中等 | 链表 · 快慢指针 / 数学 | [📝](notes/22-环形链表%20II.md) | [🐍](solutions/环形链表%20II.py) |
| 23 | [每日温度](https://leetcode.cn/problems/daily-temperatures/) | 中等 | 数组 · 单调栈 | [📝](notes/23-每日温度.md) | [🐍](solutions/每日温度.py) |
| 24 | [二叉树的层序遍历](https://leetcode.cn/problems/binary-tree-level-order-traversal/) | 中等 | 树 · 广度优先搜索 | [📝](notes/24-二叉树的层序遍历.md) | [🐍](solutions/二叉树的层序遍历.py) |
| 25 | [缺失的第一个正数](https://leetcode.cn/problems/first-missing-positive/) | 困难 | 数组 · 原地哈希 | [📝](notes/25-缺失的第一个正数.md) | [🐍](solutions/缺失的第一个正数.py) |
| 26 | [两数相加](https://leetcode.cn/problems/add-two-numbers/) | 中等 | 链表 · 递归 / 进位 | [📝](notes/26-两数相加.md) | [🐍](solutions/两数相加.py) |
| 27 | [合并两个有序链表](https://leetcode.cn/problems/merge-two-sorted-lists/) | 简单 | 链表 · 双指针 / 归并 | [📝](notes/27-合并两个有序链表.md) | [🐍](solutions/合并两个有序链表.py) |
| 28 | [二进制位得分](https://leetcode.cn/problems/binary-digit-score/) | 简单 | 位运算 · popcount | [📝](notes/28-二进制位得分.md) | [🐍](solutions/二进制位得分.py) |
| 29 | [柱状图中最大的矩形](https://leetcode.cn/problems/largest-rectangle-in-histogram/) | 困难 | 数组 · 单调栈 | [📝](notes/29-柱状图中最大的矩形.md) | [🐍](solutions/柱状图中最大的矩形.py) |
| 30 | [验证二叉搜索树](https://leetcode.cn/problems/validate-binary-search-tree/) | 中等 | 树 · 上下界 DFS / 中序遍历 | [📝](notes/30-验证二叉搜索树.md) | [🐍](solutions/验证二叉搜索树.py) |
| 31 | [合并整数后的最小值](https://leetcode.cn/problems/minimum-value-of-merged-integers/) | 简单 | 数组 · 模拟 / 字符串拼接 | [📝](notes/31-合并整数后的最小值.md) | [🐍](solutions/合并整数后的最小值.py) |
| 32 | [找到字符串中所有字母异位词](https://leetcode.cn/problems/find-all-anagrams-in-a-string/) | 中等 | 字符串 · 滑动窗口 / 计数 | [📝](notes/32-找到字符串中所有字母异位词.md) | [🐍](solutions/找到字符串中所有字母异位词.py) |
| 33 | [最长连续序列](https://leetcode.cn/problems/longest-consecutive-sequence/) | 中等 | 数组 · 哈希集合 | [📝](notes/33-最长连续序列.md) | [🐍](solutions/最长连续序列.py) |
| 34 | [删除链表的倒数第 N 个结点](https://leetcode.cn/problems/remove-nth-node-from-end-of-list/) | 中等 | 链表 · 双指针 | [📝](notes/34-删除链表的倒数第 N 个结点.md) | [🐍](solutions/删除链表的倒数第 N 个结点.py) |
| 35 | [二叉搜索树中第 K 小的元素](https://leetcode.cn/problems/kth-smallest-element-in-a-bst/) | 中等 | 树 · 中序遍历 / BST | [📝](notes/35-二叉搜索树中第K小的元素.md) | [🐍](solutions/二叉搜索树中第K小的元素.py) |
| 36 | [二叉树的右视图](https://leetcode.cn/problems/binary-tree-right-side-view/) | 中等 | 树 · DFS 右优先 / BFS | [📝](notes/36-二叉树的右视图.md) | [🐍](solutions/二叉树的右视图.py) |
| 37 | [爬楼梯](https://leetcode.cn/problems/climbing-stairs/) | 简单 | 动态规划 · 斐波那契递推 | [📝](notes/37-爬楼梯.md) | [🐍](solutions/爬楼梯.py) |
| 38 | [移动零](https://leetcode.cn/problems/move-zeroes/) | 简单 | 数组 · 双指针 / 原地交换 | [📝](notes/38-移动零.md) | [🐍](solutions/移动零.py) |
| 39 | [和为 K 的子数组](https://leetcode.cn/problems/subarray-sum-equals-k/) | 中等 | 数组 · 前缀和 / 哈希表 | [📝](notes/39-和为 K 的子数组.md) | [🐍](solutions/和为 K 的子数组.py) |
| 40 | [两两交换链表中的节点](https://leetcode.cn/problems/swap-nodes-in-pairs/) | 中等 | 链表 · 递归 / 指针操作 | [📝](notes/40-两两交换链表中的节点.md) | [🐍](solutions/两两交换链表中的节点.py) |
| 41 | [随机链表的复制](https://leetcode.cn/problems/copy-list-with-random-pointer/) | 中等 | 链表 · 哈希表 / 深拷贝 | [📝](notes/41-随机链表的复制.md) | [🐍](solutions/随机链表的复制.py) |
| 42 | [杨辉三角](https://leetcode.cn/problems/pascals-triangle/) | 简单 | 数组 · 动态规划 / 递推 | [📝](notes/42-杨辉三角.md) | [🐍](solutions/杨辉三角.py) |
| 43 | [只出现一次的数字](https://leetcode.cn/problems/single-number/) | 简单 | 位运算 · 异或 | [📝](notes/43-只出现一次的数字.md) | [🐍](solutions/只出现一次的数字.py) |
| 44 | [二叉树展开为链表](https://leetcode.cn/problems/flatten-binary-tree-to-linked-list/) | 中等 | 树 · 前序遍历 / 指针重接 | [📝](notes/44-二叉树展开为链表.md) | [🐍](solutions/二叉树展开为链表.py) |
| 45 | [三数之和](https://leetcode.cn/problems/3sum/) | 中等 | 数组 · 排序 / 双指针 | [📝](notes/45-三数之和.md) | [🐍](solutions/三数之和.py) |
| 46 | [盛最多水的容器](https://leetcode.cn/problems/container-with-most-water/) | 中等 | 数组 · 双指针 / 贪心 | [📝](notes/46-盛最多水的容器.md) | [🐍](solutions/盛最多水的容器.py) |

## 目录结构

```
Algorithm-Notes/
├── README.md            # 索引与约定
├── notes/               # 每道题一篇笔记（思路 + 复杂度 + 易错点）
│   ├── 01-两数之和.md
│   ├── 02-最大子数组和.md
│   ├── 03-相交链表.md
│   ├── 04-有效的括号.md
│   ├── 05-买卖股票的最佳时机.md
│   ├── 06-二叉树的中序遍历.md
│   ├── 07-二叉树的最大深度.md
│   ├── 08-合并区间.md
│   ├── 09-反转链表.md
│   ├── 10-回文链表.md
│   ├── 11-字符串解码.md
│   ├── 12-反转二叉树.md
│   ├── 13-对称二叉树.md
│   ├── 14-轮转数组.md
│   ├── 15-字母异位词分组.md
│   ├── 16-环形链表.md
│   ├── 17-最小栈.md
│   ├── 18-二叉树的直径.md
│   ├── 19-将有序数组转换为二叉搜索树.md
│   ├── 20-无重复字符的最长子串.md
│   ├── 21-除了自身以外数组的乘积.md
│   ├── 22-环形链表 II.md
│   ├── 23-每日温度.md
│   ├── 24-二叉树的层序遍历.md
│   ├── 25-缺失的第一个正数.md
│   ├── 26-两数相加.md
│   ├── 27-合并两个有序链表.md
│   ├── 28-二进制位得分.md
│   ├── 29-柱状图中最大的矩形.md
│   ├── 30-验证二叉搜索树.md
│   ├── 31-合并整数后的最小值.md
│   ├── 32-找到字符串中所有字母异位词.md
│   ├── 33-最长连续序列.md
│   ├── 34-删除链表的倒数第 N 个结点.md
│   ├── 35-二叉搜索树中第K小的元素.md
│   ├── 36-二叉树的右视图.md
│   ├── 37-爬楼梯.md
│   ├── 38-移动零.md
│   ├── 39-和为 K 的子数组.md
│   ├── 40-两两交换链表中的节点.md
│   ├── 41-随机链表的复制.md
│   ├── 42-杨辉三角.md
│   ├── 43-只出现一次的数字.md
│   ├── 44-二叉树展开为链表.md
│   ├── 45-三数之和.md
│   └── 46-盛最多水的容器.md
├── solutions/           # 对应题目的 Python 实现
│   ├── 两数之和.py
│   ├── 最大子数组和.py
│   ├── 相交链表.py
│   ├── 有效的括号.py
│   ├── 买卖股票的最佳时机.py
│   ├── 二叉树的中序遍历.py
│   ├── 二叉树的最大深度.py
│   ├── 合并区间.py
│   ├── 反转链表.py
│   ├── 回文链表.py
│   ├── 字符串解码.py
│   ├── 反转二叉树.py
│   ├── 对称二叉树.py
│   ├── 轮转数组.py
│   ├── 字母异位词分组.py
│   ├── 环形链表.py
│   ├── 最小栈.py
│   ├── 二叉树的直径.py
│   ├── 将有序数组转换为二叉搜索树.py
│   ├── 无重复字符的最长子串.py
│   ├── 除了自身以外数组的乘积.py
│   ├── 环形链表 II.py
│   ├── 每日温度.py
│   ├── 二叉树的层序遍历.py
│   ├── 缺失的第一个正数.py
│   ├── 两数相加.py
│   ├── 合并两个有序链表.py
│   ├── 二进制位得分.py
│   ├── 柱状图中最大的矩形.py
│   ├── 验证二叉搜索树.py
│   ├── 合并整数后的最小值.py
│   ├── 找到字符串中所有字母异位词.py
│   ├── 最长连续序列.py
│   ├── 删除链表的倒数第 N 个结点.py
│   ├── 二叉搜索树中第K小的元素.py
│   ├── 二叉树的右视图.py
│   ├── 爬楼梯.py
│   ├── 移动零.py
│   ├── 和为 K 的子数组.py
│   ├── 两两交换链表中的节点.py
│   ├── 随机链表的复制.py
│   ├── 杨辉三角.py
│   ├── 只出现一次的数字.py
│   ├── 二叉树展开为链表.py
│   ├── 三数之和.py
│   └── 盛最多水的容器.py
└── tests/
    └── test_solutions.py   # 全部用例，可直接运行
```

## 运行测试

零依赖，两种方式都行：

```bash
python tests/test_solutions.py      # 直接跑
python -m pytest tests/ -v          # 装了 pytest 的话
```

## 笔记模板

每篇笔记统一按下面六段组织，保证查阅时的心智模型一致：

1. **题目** —— 一句话概括，标注来源与难度
2. **思路** —— 从暴力解推到最优解，写清「为什么这样想」
3. **复杂度** —— 时间 / 空间，说明依据
4. **代码** —— 带注释的实现
5. **易错点** —— 自己踩过的坑、边界情况
6. **相关题目** —— 可以一起刷的同类题

## 约定

- 代码统一使用 LeetCode 的 `class Solution` 形式，方便直接粘贴提交
- 文件名与题目中文名保持一致，编号前缀用于排序
- 测试用例按题目分子函数，新增题解时同步补充测试
