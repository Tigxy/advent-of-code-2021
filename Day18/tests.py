from utils import *

magnitude_tests = [
    ("[[1,2],[[3,4],5]]", 143),
    ("[[[[0,7],4],[[7,8],[6,0]]],[8,1]]", 1384),
    ("[[[[1,1],[2,2]],[3,3]],[4,4]]", 445),
    ("[[[[3,0],[5,3]],[4,4]],[5,5]]", 791),
    ("[[[[5,0],[7,4]],[5,5]],[6,6]]", 1137),
    ("[[[[8,7],[7,7]],[[8,6],[7,7]]],[[[0,7],[6,6]],[8,7]]]", 3488)
]

# ensure that magnitude calculation and parsing works
for s, v in magnitude_tests:
    expr = parse(s)
    magnitude = eval_magnitude(expr)
    assert magnitude == v

expr = parse("[[1,2],[[3,4],5]]")
root = create_tree(expr)
get_next(root.right.left.left, next_left=True)

explode_tests = [
    ("[[[[[9,8],1],2],3],4]", "[[[[0,9],2],3],4]"),
    ("[7,[6,[5,[4,[3,2]]]]]", "[7,[6,[5,[7,0]]]]"),
    ("[[6,[5,[4,[3,2]]]],1]", "[[6,[5,[7,0]]],3]"),
    ("[[3,[2,[1,[7,3]]]],[6,[5,[4,[3,2]]]]]", "[[3,[2,[8,0]]],[9,[5,[4,[3,2]]]]]"),
    ("[[3,[2,[8,0]]],[9,[5,[4,[3,2]]]]]", "[[3,[2,[8,0]]],[9,[5,[7,0]]]]")
]

for orig, expl in explode_tests:
    orig = create_tree(parse(orig))

    assert reduce(orig)
    assert str(orig) == expl, f"{orig} != {expl}"

a = "[[[[4,3],4],4],[7,[[8,4],9]]]"
b = "[1,1]"

root = add_nodes(a, b)
print("after add:", root)
while True:
    result = reduce(root)
    if result:
        print(f"after {result}: {root}")
    else:
        break

print()
