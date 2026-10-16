# Algorithm-Notes

个人算法刷题笔记 —— 记录每道题的**思路推导**、**复杂度分析**、**易错点**与**可运行代码**。

> 目标不是「抄一份 AC 代码」，而是留下「下次遇到同类题能想起怎么下手」的线索。

## 题目索引

| # | 题目 | 难度 | 核心考点 | 笔记 | 代码 |
|---|------|:----:|----------|:----:|:----:|
| 1 | [两数之和](https://leetcode.cn/problems/two-sum/) | 简单 | 哈希表 · 空间换时间 | [📝](notes/01-两数之和.md) | [🐍](solutions/两数之和.py) |
| 2 | [最大子数组和](https://leetcode.cn/problems/maximum-subarray/) | 中等 | 动态规划 · Kadane 算法 | [📝](notes/02-最大子数组和.md) | [🐍](solutions/最大子数组和.py) |
| 3 | [相交链表](https://leetcode.cn/problems/intersection-of-two-linked-lists/) | 简单 | 链表 · 哈希集合 / 双指针 | [📝](notes/03-相交链表.md) | [🐍](solutions/相交链表.py) |

## 目录结构

```
Algorithm-Notes/
├── README.md            # 索引与约定
├── notes/               # 每道题一篇笔记（思路 + 复杂度 + 易错点）
│   ├── 01-两数之和.md
│   ├── 02-最大子数组和.md
│   └── 03-相交链表.md
├── solutions/           # 对应题目的 Python 实现
│   ├── 两数之和.py
│   ├── 最大子数组和.py
│   └── 相交链表.py
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
