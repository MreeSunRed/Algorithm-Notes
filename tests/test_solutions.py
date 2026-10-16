# -*- coding: utf-8 -*-
"""Algorithm-Notes 测试用例。

零依赖，两种运行方式皆可：

    python tests/test_solutions.py
    python -m pytest tests/ -v
"""

import importlib.util
import os
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SOLUTIONS_DIR = os.path.join(ROOT, "solutions")


def _load(module_name, filename):
    """按文件路径加载题解模块（文件名含中文，不能用普通 import）。"""
    path = os.path.join(SOLUTIONS_DIR, filename)
    spec = importlib.util.spec_from_file_location(module_name, path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


class ListNode(object):
    """与 LeetCode 定义一致的单链表节点。"""

    def __init__(self, x):
        self.val = x
        self.next = None


def make_list(values):
    """由 Python 列表构造单链表，返回头节点。"""
    head = tail = None
    for v in values:
        node = ListNode(v)
        if head is None:
            head = node
        else:
            tail.next = node
        tail = node
    return head


def append_to(head, node):
    """把 node 接到 head 所在链表的末尾。"""
    if head is None:
        return node
    cur = head
    while cur.next:
        cur = cur.next
    cur.next = node
    return head


# ---------------------------------------------------------------- 1. 两数之和

def test_two_sum_basic():
    Solution = _load("two_sum", "两数之和.py").Solution
    assert sorted(Solution().twoSum([2, 7, 11, 15], 9)) == [0, 1]


def test_two_sum_duplicate_values():
    """重复元素：不能返回同一个下标两次。"""
    Solution = _load("two_sum", "两数之和.py").Solution
    assert sorted(Solution().twoSum([3, 3], 6)) == [0, 1]


def test_two_sum_answer_at_end():
    """答案在末尾 —— 覆盖字典需要存下大量元素的分支。"""
    Solution = _load("two_sum", "两数之和.py").Solution
    assert sorted(Solution().twoSum([1, 2, 3, 4, 10], 14)) == [3, 4]


def test_two_sum_with_negative():
    Solution = _load("two_sum", "两数之和.py").Solution
    assert sorted(Solution().twoSum([-3, 4, 3, 90], 0)) == [0, 2]


# ------------------------------------------------------------ 2. 最大子数组和

def test_max_subarray_classic():
    Solution = _load("max_subarray", "最大子数组和.py").Solution
    assert Solution().maxSubArray([-2, 1, -3, 4, -1, 2, 1, -5, 4]) == 6


def test_max_subarray_single():
    Solution = _load("max_subarray", "最大子数组和.py").Solution
    assert Solution().maxSubArray([1]) == 1


def test_max_subarray_all_negative():
    """全负数 —— 最容易被 maxnum 初始化成 0 坑掉的用例。"""
    Solution = _load("max_subarray", "最大子数组和.py").Solution
    assert Solution().maxSubArray([-2, -1, -3]) == -1
    assert Solution().maxSubArray([-5]) == -5


def test_max_subarray_whole_array():
    Solution = _load("max_subarray", "最大子数组和.py").Solution
    assert Solution().maxSubArray([5, 4, -1, 7, 8]) == 23


def test_max_subarray_single_positive():
    Solution = _load("max_subarray", "最大子数组和.py").Solution
    assert Solution().maxSubArray([-1, -2, 5, -1]) == 5


# -------------------------------------------------------------- 3. 相交链表

def test_intersection_exists():
    Solution = _load("intersection", "相交链表.py").Solution

    common = make_list([8, 4, 5])
    head_a = append_to(make_list([4, 1]), common)
    head_b = append_to(make_list([5, 6, 1]), common)

    assert Solution().getIntersectionNode(head_a, head_b) is common


def test_intersection_at_head():
    """其中一个链表的头就是交点。"""
    Solution = _load("intersection", "相交链表.py").Solution

    common = make_list([1, 2, 3])
    head_a = common
    head_b = append_to(make_list([9, 9]), common)

    assert Solution().getIntersectionNode(head_a, head_b) is common


def test_no_intersection():
    Solution = _load("intersection", "相交链表.py").Solution

    head_a = make_list([2, 6, 4])
    head_b = make_list([1, 5])

    assert Solution().getIntersectionNode(head_a, head_b) is None


def test_same_values_but_no_intersection():
    """值全相同但不是同一批节点 —— 必须按身份比较，不能按 val。"""
    Solution = _load("intersection", "相交链表.py").Solution

    head_a = make_list([1, 2, 3])
    head_b = make_list([1, 2, 3])

    assert Solution().getIntersectionNode(head_a, head_b) is None


def test_intersection_returns_first_node():
    """必须返回第一个交点，而不是共享段的最后一个节点。"""
    Solution = _load("intersection", "相交链表.py").Solution

    common = make_list([1, 2, 3])
    head_a = append_to(make_list([7]), common)
    head_b = append_to(make_list([9]), common)

    result = Solution().getIntersectionNode(head_a, head_b)
    assert result is common
    assert result.val == 1


# ------------------------------------------------------------------ 运行入口

def _run_all():
    tests = [(name, fn) for name, fn in sorted(globals().items())
             if name.startswith("test_") and callable(fn)]
    passed, failed = 0, []

    for name, fn in tests:
        try:
            fn()
            passed += 1
            print("  PASS  {}".format(name))
        except AssertionError as exc:
            failed.append(name)
            print("  FAIL  {}  <- 断言失败 {}".format(name, exc))
        except Exception as exc:  # noqa: BLE001
            failed.append(name)
            print("  ERROR {}  <- {}: {}".format(name, type(exc).__name__, exc))

    print("\n{} passed, {} failed, {} total".format(passed, len(failed), len(tests)))
    return 1 if failed else 0


if __name__ == "__main__":
    sys.exit(_run_all())
