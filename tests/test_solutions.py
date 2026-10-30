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


def list_values(head):
    """把链表节点值摊平成 Python 列表，便于断言。"""
    values = []
    while head:
        values.append(head.val)
        head = head.next
    return values


def level_order(root):
    """按 LeetCode 层序格式输出二叉树，去掉末尾的空位。"""
    if root is None:
        return []
    result = []
    queue = deque([root])
    while queue:
        node = queue.popleft()
        if node is None:
            result.append(None)
            continue
        result.append(node.val)
        queue.append(node.left)
        queue.append(node.right)
    while result and result[-1] is None:
        result.pop()
    return result


def make_cycle(values, pos):
    """按 pos 把链表尾接到指定下标，构造带环链表；pos < 0 表示无环。"""
    head = make_list(values)
    if pos < 0 or head is None:
        return head
    nodes = []
    cur = head
    while cur:
        nodes.append(cur)
        cur = cur.next
    nodes[-1].next = nodes[pos]
    return head


def normalize_groups(groups):
    """把分组结果归一化，忽略组间顺序与组内顺序。"""
    return sorted(sorted(group) for group in groups)


def node_at(head, index):
    """返回从 head 起第 index 个节点（0 基）。"""
    cur = head
    for _ in range(index):
        cur = cur.next
    return cur


def inorder_values(root):
    """返回二叉树的中序遍历值序列。"""
    if root is None:
        return []
    return inorder_values(root.left) + [root.val] + inorder_values(root.right)


def tree_height(root):
    """返回二叉树的高度（按节点数计）。"""
    if root is None:
        return 0
    return 1 + max(tree_height(root.left), tree_height(root.right))


def is_balanced(root):
    """判断二叉树是否高度平衡。"""
    if root is None:
        return True
    return (abs(tree_height(root.left) - tree_height(root.right)) <= 1
            and is_balanced(root.left)
            and is_balanced(root.right))


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


# ---------------------------------------------------------------- 9. 反转链表

def test_reverse_empty():
    Solution = _load("reverse_list", "反转链表.py").Solution
    assert Solution().reverseList(None) is None


def test_reverse_single():
    Solution = _load("reverse_list", "反转链表.py").Solution
    result = Solution().reverseList(make_list([1]))
    assert list_values(result) == [1]


def test_reverse_two():
    Solution = _load("reverse_list", "反转链表.py").Solution
    result = Solution().reverseList(make_list([1, 2]))
    assert list_values(result) == [2, 1]


def test_reverse_multiple():
    Solution = _load("reverse_list", "反转链表.py").Solution
    result = Solution().reverseList(make_list([1, 2, 3, 4, 5]))
    assert list_values(result) == [5, 4, 3, 2, 1]


def test_reverse_duplicates():
    """值重复也要按节点顺序反转，不能按值去重。"""
    Solution = _load("reverse_list", "反转链表.py").Solution
    result = Solution().reverseList(make_list([1, 1, 2, 1]))
    assert list_values(result) == [1, 2, 1, 1]


# -------------------------------------------------------------- 10. 回文链表

def test_palindrome_even():
    Solution = _load("palindrome_list", "回文链表.py").Solution
    assert Solution().isPalindrome(make_list([1, 2, 2, 1])) is True


def test_palindrome_odd():
    Solution = _load("palindrome_list", "回文链表.py").Solution
    assert Solution().isPalindrome(make_list([1, 2, 3, 2, 1])) is True


def test_palindrome_single():
    Solution = _load("palindrome_list", "回文链表.py").Solution
    assert Solution().isPalindrome(make_list([1])) is True


def test_palindrome_empty():
    """LeetCode 保证至少一个节点；空链表按回文处理，实现天然兼容。"""
    Solution = _load("palindrome_list", "回文链表.py").Solution
    assert Solution().isPalindrome(None) is True


def test_palindrome_two_nodes():
    Solution = _load("palindrome_list", "回文链表.py").Solution
    assert Solution().isPalindrome(make_list([1, 2])) is False
    assert Solution().isPalindrome(make_list([1, 1])) is True


def test_palindrome_broken_mirror():
    Solution = _load("palindrome_list", "回文链表.py").Solution
    assert Solution().isPalindrome(make_list([1, 1, 2, 1])) is False
    assert Solution().isPalindrome(make_list([1, 2, 1, 1])) is False


def test_palindrome_with_negative():
    Solution = _load("palindrome_list", "回文链表.py").Solution
    assert Solution().isPalindrome(make_list([-1, 0, -1])) is True


# -------------------------------------------------------------- 11. 字符串解码

def test_decode_basic():
    Solution = _load("decode_string", "字符串解码.py").Solution
    assert Solution().decodeString("3[a]2[bc]") == "aaabcbc"
    assert Solution().decodeString("3[a]") == "aaa"


def test_decode_nested():
    Solution = _load("decode_string", "字符串解码.py").Solution
    assert Solution().decodeString("3[a2[c]]") == "accaccacc"
    assert Solution().decodeString("2[3[a]]") == "aaaaaa"


def test_decode_mixed_with_plain_chars():
    Solution = _load("decode_string", "字符串解码.py").Solution
    assert Solution().decodeString("2[abc]3[cd]ef") == "abcabccdcdcdef"
    assert Solution().decodeString("abc3[cd]xyz") == "abccdcdcdxyz"


def test_decode_multi_digit():
    """重复次数可能是多位数，不能只取一位。"""
    Solution = _load("decode_string", "字符串解码.py").Solution
    assert Solution().decodeString("10[a]") == "a" * 10
    assert Solution().decodeString("2[10[b]]") == "b" * 20


def test_decode_plain_text():
    Solution = _load("decode_string", "字符串解码.py").Solution
    assert Solution().decodeString("") == ""
    assert Solution().decodeString("a") == "a"
    assert Solution().decodeString("abc") == "abc"


# -------------------------------------------------------------- 12. 反转二叉树

def test_invert_classic():
    Solution = _load("invert_tree", "反转二叉树.py").Solution
    result = Solution().invertTree(make_tree([4, 2, 7, 1, 3, 6, 9]))
    assert level_order(result) == [4, 7, 2, 9, 6, 3, 1]


def test_invert_empty():
    Solution = _load("invert_tree", "反转二叉树.py").Solution
    assert Solution().invertTree(None) is None


def test_invert_single():
    Solution = _load("invert_tree", "反转二叉树.py").Solution
    result = Solution().invertTree(make_tree([1]))
    assert level_order(result) == [1]


def test_invert_single_child():
    """只有一个孩子时，翻转会把孩子换到另一侧。"""
    Solution = _load("invert_tree", "反转二叉树.py").Solution
    left_only = Solution().invertTree(make_tree([1, 2]))
    assert level_order(left_only) == [1, None, 2]

    right_only = Solution().invertTree(make_tree([1, None, 2]))
    assert level_order(right_only) == [1, 2]


def test_invert_twice_restores():
    Solution = _load("invert_tree", "反转二叉树.py").Solution
    root = make_tree([4, 2, 7, 1, 3, 6, 9])
    solution = Solution()
    solution.invertTree(root)
    solution.invertTree(root)
    assert level_order(root) == [4, 2, 7, 1, 3, 6, 9]


# -------------------------------------------------------------- 13. 对称二叉树

def test_symmetric_classic():
    Solution = _load("symmetric_tree", "对称二叉树.py").Solution
    assert Solution().isSymmetric(make_tree([1, 2, 2, 3, 4, 4, 3])) is True


def test_symmetric_wrong_structure():
    """值相同但左右的结构不对应，必须交叉比较。"""
    Solution = _load("symmetric_tree", "对称二叉树.py").Solution
    assert Solution().isSymmetric(make_tree([1, 2, 2, None, 3, None, 3])) is False


def test_symmetric_empty_and_single():
    Solution = _load("symmetric_tree", "对称二叉树.py").Solution
    assert Solution().isSymmetric(None) is True
    assert Solution().isSymmetric(make_tree([1])) is True


def test_symmetric_simple():
    Solution = _load("symmetric_tree", "对称二叉树.py").Solution
    assert Solution().isSymmetric(make_tree([1, 2, 2])) is True
    assert Solution().isSymmetric(make_tree([1, 2, 3])) is False


def test_symmetric_inorder_palindrome_not_enough():
    """中序遍历是回文但结构不对称 —— 不能只比较中序序列。"""
    Solution = _load("symmetric_tree", "对称二叉树.py").Solution
    root = make_tree([1, 2, 2, 2, None, 2])
    assert Solution().isSymmetric(root) is False


# ---------------------------------------------------------------- 14. 轮转数组

def test_rotate_classic():
    Solution = _load("rotate_array", "轮转数组.py").Solution
    nums = [1, 2, 3, 4, 5, 6, 7]
    result = Solution().rotate(nums, 3)
    assert nums == [5, 6, 7, 1, 2, 3, 4]
    assert result is None


def test_rotate_with_negative():
    Solution = _load("rotate_array", "轮转数组.py").Solution
    nums = [-1, -100, 3, 99]
    Solution().rotate(nums, 2)
    assert nums == [3, 99, -1, -100]


def test_rotate_single():
    Solution = _load("rotate_array", "轮转数组.py").Solution
    nums = [1]
    Solution().rotate(nums, 0)
    assert nums == [1]

    nums = [1]
    Solution().rotate(nums, 5)
    assert nums == [1]


def test_rotate_k_greater_than_length():
    """k 大于 n 时等价于转 k % n 次。"""
    Solution = _load("rotate_array", "轮转数组.py").Solution
    nums = [1, 2]
    Solution().rotate(nums, 3)
    assert nums == [2, 1]

    nums = [1, 2, 3]
    Solution().rotate(nums, 5)
    assert nums == [2, 3, 1]


def test_rotate_k_multiple_of_length():
    """k 是 n 的整数倍，数组应保持不变。"""
    Solution = _load("rotate_array", "轮转数组.py").Solution
    nums = [1, 2, 3, 4]
    Solution().rotate(nums, 4)
    assert nums == [1, 2, 3, 4]

    nums = [1, 2, 3, 4]
    Solution().rotate(nums, 8)
    assert nums == [1, 2, 3, 4]


def test_rotate_zero():
    Solution = _load("rotate_array", "轮转数组.py").Solution
    nums = [1, 2, 3]
    Solution().rotate(nums, 0)
    assert nums == [1, 2, 3]


# --------------------------------------------------------- 15. 字母异位词分组

def test_group_anagrams_classic():
    Solution = _load("group_anagrams", "字母异位词分组.py").Solution
    groups = Solution().groupAnagrams(
        ["eat", "tea", "tan", "ate", "nat", "bat"]
    )
    assert normalize_groups(groups) == [
        ["ate", "eat", "tea"],
        ["bat"],
        ["nat", "tan"],
    ]


def test_group_anagrams_empty_input():
    Solution = _load("group_anagrams", "字母异位词分组.py").Solution
    assert Solution().groupAnagrams([]) == []


def test_group_anagrams_empty_string():
    Solution = _load("group_anagrams", "字母异位词分组.py").Solution
    assert Solution().groupAnagrams([""]) == [[""]]


def test_group_anagrams_single():
    Solution = _load("group_anagrams", "字母异位词分组.py").Solution
    assert Solution().groupAnagrams(["a"]) == [["a"]]


def test_group_anagrams_multiple_groups():
    Solution = _load("group_anagrams", "字母异位词分组.py").Solution
    groups = Solution().groupAnagrams(["abc", "bca", "cab", "xyz"])
    assert normalize_groups(groups) == [
        ["abc", "bca", "cab"],
        ["xyz"],
    ]


def test_group_anagrams_do_not_merge_different_counts():
    """字母种类不同，即使长度相同也不能合并。"""
    Solution = _load("group_anagrams", "字母异位词分组.py").Solution
    groups = Solution().groupAnagrams(["ddddddddddg", "dgggggggggg"])
    assert normalize_groups(groups) == [
        ["ddddddddddg"],
        ["dgggggggggg"],
    ]


# ---------------------------------------------------------------- 16. 环形链表

def test_cycle_empty():
    Solution = _load("linked_list_cycle", "环形链表.py").Solution
    assert Solution().hasCycle(None) is False


def test_cycle_single_no_cycle():
    Solution = _load("linked_list_cycle", "环形链表.py").Solution
    assert Solution().hasCycle(make_cycle([1], -1)) is False


def test_cycle_single_self_loop():
    Solution = _load("linked_list_cycle", "环形链表.py").Solution
    assert Solution().hasCycle(make_cycle([1], 0)) is True


def test_cycle_classic():
    Solution = _load("linked_list_cycle", "环形链表.py").Solution
    assert Solution().hasCycle(make_cycle([3, 2, 0, -4], 1)) is True


def test_cycle_no_cycle():
    Solution = _load("linked_list_cycle", "环形链表.py").Solution
    assert Solution().hasCycle(make_cycle([1, 2, 3], -1)) is False


def test_cycle_duplicate_values_without_cycle():
    """值重复但节点不重复，不能按 val 判环。"""
    Solution = _load("linked_list_cycle", "环形链表.py").Solution
    assert Solution().hasCycle(make_cycle([1, 1], -1)) is False


# ---------------------------------------------------------------- 17. 最小栈

def test_min_stack_classic():
    MinStack = _load("min_stack", "最小栈.py").MinStack
    stack = MinStack()
    stack.push(-2)
    stack.push(0)
    stack.push(-3)
    assert stack.getMin() == -3
    assert stack.pop() is None
    assert stack.top() == 0
    assert stack.getMin() == -2


def test_min_stack_single():
    MinStack = _load("min_stack", "最小栈.py").MinStack
    stack = MinStack()
    stack.push(5)
    assert stack.top() == 5
    assert stack.getMin() == 5
    assert stack.pop() is None


def test_min_stack_duplicates():
    """重复最小值：弹出一个后，getMin 仍应正确。"""
    MinStack = _load("min_stack", "最小栈.py").MinStack
    stack = MinStack()
    stack.push(0)
    stack.push(0)
    assert stack.getMin() == 0
    stack.pop()
    assert stack.top() == 0
    assert stack.getMin() == 0


def test_min_stack_negative():
    MinStack = _load("min_stack", "最小栈.py").MinStack
    stack = MinStack()
    stack.push(-1)
    stack.push(-2)
    stack.push(-3)
    assert stack.getMin() == -3
    stack.pop()
    assert stack.getMin() == -2
    stack.pop()
    assert stack.getMin() == -1


def test_min_stack_push_larger():
    """压入更大的值不改变当前最小值。"""
    MinStack = _load("min_stack", "最小栈.py").MinStack
    stack = MinStack()
    stack.push(2)
    stack.push(3)
    assert stack.top() == 3
    assert stack.getMin() == 2
    stack.pop()
    assert stack.top() == 2
    assert stack.getMin() == 2


# ---------------------------------------------------------- 18. 二叉树的直径

def test_diameter_single():
    Solution = _load("tree_diameter", "二叉树的直径.py").Solution
    assert Solution().diameterOfBinaryTree(make_tree([1])) == 0


def test_diameter_two_nodes():
    Solution = _load("tree_diameter", "二叉树的直径.py").Solution
    assert Solution().diameterOfBinaryTree(make_tree([1, 2])) == 1


def test_diameter_three_nodes():
    Solution = _load("tree_diameter", "二叉树的直径.py").Solution
    assert Solution().diameterOfBinaryTree(make_tree([1, 2, 3])) == 2


def test_diameter_classic():
    Solution = _load("tree_diameter", "二叉树的直径.py").Solution
    root = make_tree([1, 2, 3, 4, 5])
    assert Solution().diameterOfBinaryTree(root) == 3


def test_diameter_skewed():
    """退化成链：直径就是链上的边数。"""
    Solution = _load("tree_diameter", "二叉树的直径.py").Solution
    root = make_tree([1, 2, None, 3, None, 4])
    assert Solution().diameterOfBinaryTree(root) == 3


# -------------------------------------- 19. 将有序数组转换为二叉搜索树

def test_sorted_array_empty():
    Solution = _load("sorted_array_to_bst",
                     "将有序数组转换为二叉搜索树.py").Solution
    assert Solution().sortedArrayToBST([]) is None


def test_sorted_array_single():
    Solution = _load("sorted_array_to_bst",
                     "将有序数组转换为二叉搜索树.py").Solution
    root = Solution().sortedArrayToBST([1])
    assert inorder_values(root) == [1]
    assert tree_height(root) == 1


def test_sorted_array_classic():
    """结果不唯一：验证中序序列与平衡性，而不是固定形状。"""
    Solution = _load("sorted_array_to_bst",
                     "将有序数组转换为二叉搜索树.py").Solution
    nums = [-10, -3, 0, 5, 9]
    root = Solution().sortedArrayToBST(nums)
    assert inorder_values(root) == nums
    assert is_balanced(root) is True


def test_sorted_array_perfect():
    Solution = _load("sorted_array_to_bst",
                     "将有序数组转换为二叉搜索树.py").Solution
    nums = [1, 2, 3, 4, 5, 6, 7]
    root = Solution().sortedArrayToBST(nums)
    assert inorder_values(root) == nums
    assert is_balanced(root) is True
    assert tree_height(root) == 3


def test_sorted_array_even_length():
    Solution = _load("sorted_array_to_bst",
                     "将有序数组转换为二叉搜索树.py").Solution
    root = Solution().sortedArrayToBST([1, 2])
    assert inorder_values(root) == [1, 2]
    assert is_balanced(root) is True


# ---------------------------------------------- 20. 无重复字符的最长子串

def test_longest_substring_classic():
    Solution = _load("longest_substring",
                     "无重复字符的最长子串.py").Solution
    assert Solution().lengthOfLongestSubstring("abcabcbb") == 3


def test_longest_substring_all_same():
    Solution = _load("longest_substring",
                     "无重复字符的最长子串.py").Solution
    assert Solution().lengthOfLongestSubstring("bbbbb") == 1


def test_longest_substring_subsequence_trap():
    """最长的是子串 "wke"，不是子序列 "pwke"。"""
    Solution = _load("longest_substring",
                     "无重复字符的最长子串.py").Solution
    assert Solution().lengthOfLongestSubstring("pwwkew") == 3


def test_longest_substring_empty_and_space():
    Solution = _load("longest_substring",
                     "无重复字符的最长子串.py").Solution
    assert Solution().lengthOfLongestSubstring("") == 0
    assert Solution().lengthOfLongestSubstring(" ") == 1


def test_longest_substring_left_never_moves_back():
    """abba：最后一次出现的 a 已在窗口外，left 不能回退。"""
    Solution = _load("longest_substring",
                     "无重复字符的最长子串.py").Solution
    assert Solution().lengthOfLongestSubstring("abba") == 2


def test_longest_substring_stale_last_occurrence():
    Solution = _load("longest_substring",
                     "无重复字符的最长子串.py").Solution
    assert Solution().lengthOfLongestSubstring("tmmzuxt") == 5


# ------------------------------------------ 21. 除了自身以外数组的乘积

def test_product_except_self_classic():
    Solution = _load("product_except_self",
                     "除了自身以外数组的乘积.py").Solution
    assert Solution().productExceptSelf([1, 2, 3, 4]) == [24, 12, 8, 6]


def test_product_except_self_with_zero():
    Solution = _load("product_except_self",
                     "除了自身以外数组的乘积.py").Solution
    assert Solution().productExceptSelf([-1, 1, 0, -3, 3]) == [0, 0, 9, 0, 0]


def test_product_except_self_multiple_zeros():
    Solution = _load("product_except_self",
                     "除了自身以外数组的乘积.py").Solution
    assert Solution().productExceptSelf([0, 0]) == [0, 0]


def test_product_except_self_two_elements():
    Solution = _load("product_except_self",
                     "除了自身以外数组的乘积.py").Solution
    assert Solution().productExceptSelf([2, 3]) == [3, 2]


def test_product_except_self_single_element():
    Solution = _load("product_except_self",
                     "除了自身以外数组的乘积.py").Solution
    assert Solution().productExceptSelf([5]) == [1]


def test_product_except_self_negative():
    Solution = _load("product_except_self",
                     "除了自身以外数组的乘积.py").Solution
    assert Solution().productExceptSelf([-2, -3, 4]) == [-12, -8, 6]


# ------------------------------------------------------------ 22. 环形链表 II

def test_cycle_entry_empty():
    Solution = _load("cycle_entry", "环形链表 II.py").Solution
    assert Solution().detectCycle(None) is None


def test_cycle_entry_single_no_cycle():
    Solution = _load("cycle_entry", "环形链表 II.py").Solution
    assert Solution().detectCycle(make_cycle([1], -1)) is None


def test_cycle_entry_single_self_loop():
    Solution = _load("cycle_entry", "环形链表 II.py").Solution
    head = make_cycle([1], 0)
    assert Solution().detectCycle(head) is head


def test_cycle_entry_classic():
    Solution = _load("cycle_entry", "环形链表 II.py").Solution
    head = make_cycle([3, 2, 0, -4], 1)
    expected = node_at(head, 1)
    assert Solution().detectCycle(head) is expected


def test_cycle_entry_at_head():
    Solution = _load("cycle_entry", "环形链表 II.py").Solution
    head = make_cycle([1, 2, 3], 0)
    assert Solution().detectCycle(head) is head


def test_cycle_entry_at_tail():
    Solution = _load("cycle_entry", "环形链表 II.py").Solution
    head = make_cycle([1, 2, 3, 4], 3)
    expected = node_at(head, 3)
    assert Solution().detectCycle(head) is expected


def test_cycle_entry_duplicate_values_without_cycle():
    """值重复但无环，不能按 val 判环。"""
    Solution = _load("cycle_entry", "环形链表 II.py").Solution
    assert Solution().detectCycle(make_cycle([1, 1, 2], -1)) is None


# ---------------------------------------------------------------- 23. 每日温度

def test_daily_temperatures_classic():
    Solution = _load("daily_temperatures", "每日温度.py").Solution
    temperatures = [73, 74, 75, 71, 69, 72, 76, 73]
    assert Solution().dailyTemperatures(temperatures) == [1, 1, 4, 2, 1, 1, 0, 0]


def test_daily_temperatures_increasing():
    Solution = _load("daily_temperatures", "每日温度.py").Solution
    assert Solution().dailyTemperatures([30, 40, 50, 60]) == [1, 1, 1, 0]


def test_daily_temperatures_decreasing():
    Solution = _load("daily_temperatures", "每日温度.py").Solution
    assert Solution().dailyTemperatures([90, 60, 30]) == [0, 0, 0]


def test_daily_temperatures_equal():
    """温度相等不算「更高」。"""
    Solution = _load("daily_temperatures", "每日温度.py").Solution
    assert Solution().dailyTemperatures([73, 73, 73]) == [0, 0, 0]


def test_daily_temperatures_single():
    Solution = _load("daily_temperatures", "每日温度.py").Solution
    assert Solution().dailyTemperatures([1]) == [0]


def test_daily_temperatures_multiple_pops():
    """一天的高温要连续解答多个历史日子。"""
    Solution = _load("daily_temperatures", "每日温度.py").Solution
    assert Solution().dailyTemperatures([70, 60, 50, 80]) == [3, 2, 1, 0]


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
