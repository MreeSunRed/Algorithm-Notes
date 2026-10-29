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
│   └── 22-环形链表 II.md
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
│   └── 环形链表 II.py
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
