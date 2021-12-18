import json
from math import floor, ceil


def parse(s):
    return json.loads(s)


def eval_magnitude(node):
    if node.value is not None:
        return node.value
    return eval_magnitude(node.left) * 3 + eval_magnitude(node.right) * 2


class Node:
    def __init__(self, left=None, right=None, value=None, depth=0):
        self.left = left
        self.right = right
        self.parent = None
        self.value = value
        self.depth = depth

    def __repr__(self):
        return str(self)

    def __str__(self):
        if self.value is not None:
            return f"{self.value}"
        else:
            return f"[{self.left},{self.right}]"


def create_tree(expr, depth=0):
    depth = depth + 1
    left_child = Node(value=expr[0], depth=depth) if isinstance(expr[0], int) else create_tree(expr[0], depth=depth)
    right_child = Node(value=expr[1], depth=depth) if isinstance(expr[1], int) else create_tree(expr[1], depth=depth)

    node = Node(left_child, right_child, depth=depth - 1)
    left_child.parent = node
    right_child.parent = node
    return node


def get_next(leaf, next_left=True):
    # go up tree until there is a left node available, first left node doesn't count
    leaf = leaf.parent
    parent = None if leaf is None else leaf.parent

    while parent is not None:
        if (parent.right if next_left else parent.left) is leaf:
            node = parent.left if next_left else parent.right
            # go down tree from left node onward
            while node is not None:
                if node.value is not None:
                    return node
                else:
                    node = node.right if next_left else node.left
            return None
        else:
            leaf = parent
            parent = parent.parent
    return None


def get_leafs(node):
    if node.value is not None:
        return [node]
    return get_leafs(node.left) + get_leafs(node.right)


def get_sibling(node):
    if node.parent is None:
        return False, None
    else:
        has_left_sibling = node.parent.right is node
        return has_left_sibling, node.parent.left if has_left_sibling else node.parent.right


def reduce(node):
    leafs = get_leafs(node)
    nested_leafs = [leaf for leaf in leafs if leaf.depth > 4]

    if len(nested_leafs) > 0:
        for leaf in nested_leafs:
            is_left_sibling, sibling = get_sibling(leaf)

            # check whether pair is of numbers only
            if sibling.value is not None:
                # left sibling is added to left node, right sibling to right node
                left_node, right_node = get_next(leaf, next_left=True), get_next(leaf, next_left=False)

                # left and right nodes may be none
                if left_node is not None:
                    left_node.value += sibling.value if is_left_sibling else leaf.value
                if right_node is not None:
                    right_node.value += sibling.value if not is_left_sibling else leaf.value

                # parent is reduced to value 0
                leaf.parent.left = None
                leaf.parent.right = None
                leaf.parent.value = 0
                return "explode"

    greater_10_leafs = [leaf for leaf in leafs if leaf.value >= 10]
    if len(greater_10_leafs):
        leaf = greater_10_leafs[0]
        leaf.left = Node(value=int(floor(leaf.value / 2)), depth=leaf.depth + 1)
        leaf.right = Node(value=int(ceil(leaf.value / 2)), depth=leaf.depth + 1)
        leaf.value = None
        leaf.left.parent = leaf
        leaf.right.parent = leaf
        return "split"

    return False


def fully_reduce(node):
    while reduce(node):
        pass
    return node


def increase_depth(node):
    node.depth += 1
    if node.left:
        increase_depth(node.left)
    if node.right:
        increase_depth(node.right)


def add_nodes(first, second):
    # allow adding nodes and string expressions
    if isinstance(first, str):
        first = create_tree(parse(first))
    if isinstance(second, str):
        second = create_tree(parse(second))

    node = Node(first, second)
    first.parent = node
    second.parent = node
    increase_depth(first)
    increase_depth(second)
    return node
