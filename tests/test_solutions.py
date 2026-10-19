# -*- coding: utf-8 -*-
"""Algorithm-Notes 测试用例。

零依赖，两种运行方式皆可：

    python tests/test_solutions.py
    python -m pytest tests/ -v
"""

import importlib.util
import os
import sys
from collections import deque

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


class TreeNode(object):
    """与 LeetCode 定义一致的二叉树节点。"""

    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def make_tree(values):
    """按 LeetCode 的层序数组（None 表示空位）构造二叉树，返回根节点。"""
    if not values or values[0] is None:
        return None

    root = TreeNode(values[0])
    queue = deque([root])
    i = 1
    while queue and i < len(values):
        node = queue.popleft()
        if i < len(values) and values[i] is not None:
            node.left = TreeNode(values[i])
            queue.append(node.left)
        i += 1
        if i < len(values) and values[i] is not None:
            node.right = TreeNode(values[i])
            queue.append(node.right)
        i += 1
    return root


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


# -------------------------------------------------------------- 4. 有效的括号

def test_valid_parentheses_basic():
    Solution = _load("valid_parentheses", "有效的括号.py").Solution
    assert Solution().isValid("()") is True
    assert Solution().isValid("()[]{}") is True


def test_valid_parentheses_nested():
    Solution = _load("valid_parentheses", "有效的括号.py").Solution
    assert Solution().isValid("{[]}") is True
    assert Solution().isValid("([{}])") is True


def test_valid_parentheses_wrong_type():
    """左右括号数量对，但类型不匹配。"""
    Solution = _load("valid_parentheses", "有效的括号.py").Solution
    assert Solution().isValid("(]") is False
    assert Solution().isValid("(}") is False


def test_valid_parentheses_wrong_order():
    """数量完全相等，但闭包顺序非法 —— 只数个数会误判。"""
    Solution = _load("valid_parentheses", "有效的括号.py").Solution
    assert Solution().isValid("([)]") is False
    assert Solution().isValid("){") is False


def test_valid_parentheses_unclosed():
    """只有左括号，扫描结束时栈不为空。"""
    Solution = _load("valid_parentheses", "有效的括号.py").Solution
    assert Solution().isValid("(") is False
    assert Solution().isValid("(((") is False
    assert Solution().isValid("(()") is False


def test_valid_parentheses_extra_closing():
    """栈空时遇到右括号，不能越界取栈顶。"""
    Solution = _load("valid_parentheses", "有效的括号.py").Solution
    assert Solution().isValid(")") is False
    assert Solution().isValid("]") is False
    assert Solution().isValid("())") is False


# ------------------------------------------------------ 5. 买卖股票的最佳时机

def test_max_profit_classic():
    Solution = _load("max_profit", "买卖股票的最佳时机.py").Solution
    assert Solution().maxProfit([7, 1, 5, 3, 6, 4]) == 5


def test_max_profit_all_declining():
    """一路下跌 —— 不能交易，必须返回 0 而不是负数。"""
    Solution = _load("max_profit", "买卖股票的最佳时机.py").Solution
    assert Solution().maxProfit([7, 6, 4, 3, 1]) == 0


def test_max_profit_single():
    Solution = _load("max_profit", "买卖股票的最佳时机.py").Solution
    assert Solution().maxProfit([1]) == 0
    assert Solution().maxProfit([5]) == 0


def test_max_profit_min_after_best_sell():
    """最低价出现在最优卖出日之后，不能被提前使用。"""
    Solution = _load("max_profit", "买卖股票的最佳时机.py").Solution
    assert Solution().maxProfit([2, 4, 1]) == 2


def test_max_profit_late_min():
    Solution = _load("max_profit", "买卖股票的最佳时机.py").Solution
    assert Solution().maxProfit([3, 2, 6, 5, 0, 3]) == 4
    assert Solution().maxProfit([1, 2]) == 1


# -------------------------------------------------- 6. 二叉树的中序遍历

def test_inorder_classic():
    Solution = _load("inorder_traversal", "二叉树的中序遍历.py").Solution
    assert Solution().inorderTraversal(make_tree([1, None, 2, 3])) == [1, 3, 2]


def test_inorder_empty():
    Solution = _load("inorder_traversal", "二叉树的中序遍历.py").Solution
    assert Solution().inorderTraversal(None) == []


def test_inorder_single():
    Solution = _load("inorder_traversal", "二叉树的中序遍历.py").Solution
    assert Solution().inorderTraversal(make_tree([1])) == [1]


def test_inorder_balanced():
    Solution = _load("inorder_traversal", "二叉树的中序遍历.py").Solution
    assert Solution().inorderTraversal(make_tree([2, 1, 3])) == [1, 2, 3]


def test_inorder_bst_sorted():
    """BST 的中序遍历必须严格递增。"""
    Solution = _load("inorder_traversal", "二叉树的中序遍历.py").Solution
    root = make_tree([3, 1, None, None, 2])
    assert Solution().inorderTraversal(root) == [1, 2, 3]


def test_inorder_with_negative():
    Solution = _load("inorder_traversal", "二叉树的中序遍历.py").Solution
    root = make_tree([-1, -2, -3])
    assert Solution().inorderTraversal(root) == [-2, -1, -3]


# ---------------------------------------------------- 7. 二叉树的最大深度

def test_max_depth_classic():
    Solution = _load("max_depth", "二叉树的最大深度.py").Solution
    root = make_tree([3, 9, 20, None, None, 15, 7])
    assert Solution().maxDepth(root) == 3


def test_max_depth_empty():
    Solution = _load("max_depth", "二叉树的最大深度.py").Solution
    assert Solution().maxDepth(None) == 0


def test_max_depth_single():
    """深度按节点数算：单节点树为 1，不是 0。"""
    Solution = _load("max_depth", "二叉树的最大深度.py").Solution
    assert Solution().maxDepth(make_tree([1])) == 1


def test_max_depth_left_child_only():
    Solution = _load("max_depth", "二叉树的最大深度.py").Solution
    assert Solution().maxDepth(make_tree([1, 2])) == 2


def test_max_depth_right_chain():
    """只有右孩子的退化链。"""
    Solution = _load("max_depth", "二叉树的最大深度.py").Solution
    root = make_tree([1, None, 2, None, 3])
    assert Solution().maxDepth(root) == 3


def test_max_depth_unbalanced():
    Solution = _load("max_depth", "二叉树的最大深度.py").Solution
    root = make_tree([1, 2, 3, 4, None, None, None, 5])
    assert Solution().maxDepth(root) == 4


# ---------------------------------------------------------------- 8. 合并区间

def test_merge_classic():
    Solution = _load("merge_intervals", "合并区间.py").Solution
    intervals = [[1, 3], [2, 6], [8, 10], [15, 18]]
    assert Solution().merge(intervals) == [[1, 6], [8, 10], [15, 18]]


def test_merge_touching():
    """端点相接也算重叠：[1,4] 与 [4,5] 合并为 [1,5]。"""
    Solution = _load("merge_intervals", "合并区间.py").Solution
    assert Solution().merge([[1, 4], [4, 5]]) == [[1, 5]]


def test_merge_contained():
    """完全包含：end 必须取 max，不能缩水成 [1,3]。"""
    Solution = _load("merge_intervals", "合并区间.py").Solution
    assert Solution().merge([[1, 4], [2, 3]]) == [[1, 4]]
    assert Solution().merge([[1, 10], [2, 3], [4, 5]]) == [[1, 10]]


def test_merge_unsorted():
    Solution = _load("merge_intervals", "合并区间.py").Solution
    assert Solution().merge([[1, 4], [0, 4]]) == [[0, 4]]
    assert Solution().merge([[2, 6], [1, 3]]) == [[1, 6]]


def test_merge_no_overlap():
    Solution = _load("merge_intervals", "合并区间.py").Solution
    assert Solution().merge([[1, 4], [5, 6]]) == [[1, 4], [5, 6]]
    assert Solution().merge([[1, 2]]) == [[1, 2]]


def test_merge_empty():
    Solution = _load("merge_intervals", "合并区间.py").Solution
    assert Solution().merge([]) == []


def test_merge_many_into_one():
    Solution = _load("merge_intervals", "合并区间.py").Solution
    intervals = [[1, 10], [2, 3], [4, 5], [6, 7]]
    assert Solution().merge(intervals) == [[1, 10]]


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
