# following from YT video:
# https://www.youtube.com/watch?v=fAAZixBzIAI


class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


a = Node("a")
b = Node("b")
c = Node("c")
d = Node("d")
e = Node("e")
f = Node("f")

a.left = b
a.right = c
b.left = d
b.right = e
c.right = f

# [a, null, b, c, null, d, e, null, f]

#           a
#         / \
#        b   c
#      /  \   \
#    d    e    f


numA = Node(3)
numB = Node(11)
numC = Node(4)
numD = Node(4)
numE = Node(2)
numF = Node(30)

numA.left = numB
numA.right = numC
numB.left = numD
numB.right = numE
numC.right = numF


#       3
#     /   \
#   11     4
#  / \      \
# 4   2      30


# ____________________________________________________________
# DEPTH FIRST SEARCH

# #ITERATIVE
# DEPTH FIRST TRAVERSAL

# uncomment line 55 - 71
# def depthFirstValues(rootnode):
#     if rootnode is None:
#         return []
#     result = []
#     stack = [rootnode]
#     while len(stack) > 0:
#         current = stack.pop()
#         result.append(current.val)
## we add right then left on the stack, so left will be on top of the stack when we call stack.pop() after.
## we also guard against empty input by checking if current.right and if current.left
#         if current.right:
#             stack.append(current.right)
#         if current.left:
#             stack.append(current.left)
#     return result

# print(f"Depth first traversal (iterative) : {depthFirstValues(a)}")

# video time 29:30
# # RECURSIION
# # DEPTH FIRST TRAVERSAL
# # UNCOMMENT LINES 76 - 86
# def depthFirstRecursion(rootnode):
#     if rootnode is None:
#         return []
#     leftValues = depthFirstRecursion(rootnode.left)  # [b, d, e]
#     rightValues = depthFirstRecursion(rootnode.right)  # [c, f]
#     # *leftvalues and *rightvalues unpacks the array of values. unpacking operator: *
#     return [rootnode.val, *leftValues, *rightValues]


# print(f"Depth first traversal with recursion: {depthFirstRecursion(a)}")


# # BREADTH FIRST VALUES
# # video time: 42:22
# # no recursion because breadth first uses a queue

# UNCOMMENT LINES 101 - 117
# def breadthFirstValues(rootnode):
#     if rootnode is None:
#         return []
#     values = []
#     queue = [rootnode]
#     while len(queue) > 0:
#         current = queue.pop(0)
#         values.append(current.val)
#         ## for breadth first, we need to use a queue, so we pop off the first value in the queue, so queue.pop(0), and add left then right, instead of depth first right then left.
#         if current.left:
#             queue.append(current.left)
#         if current.right:
#             queue.append(current.right)
#     return values


# print(f"Breadth First Traversal: {breadthFirstValues(a)}")


#   ____________________________________________________________
# # TREE INCLUDES (BREADTH FIRST SEARCH ITERATIVE)
# # breadth first traversal tree includes, iterative
# # VIDEO TIME 57:20
# # UNCOMMENT LINES 126 - 142

# def treeIncludesBreadth(rootnode, target):
#     # if rootnode none, return false. without this check, we can add a "None" rootnode into queue, curent is set to None, and we check for None.val which is illegal
#     if rootnode == None:
#         return False
#     queue = [rootnode]
#     while len(queue) > 0:
#         current = queue.pop(0)
#         if current.val == target:
#             return True
#         if current.left:
#             queue.append(current.left)
#         if current.right:
#             queue.append(current.right)
#     return False


# print(f'Breadth First Tree Includes (Iterative): {treeIncludesBreadth(a, "f")}')


# # DEPTH FIRST RECURSIVE TREE INCLUDES
# VIDEO TIME: 1:02:45
# # UNCOMMENT LINES 150 - 162


# def treeIncludesRecursive(rootnode, target):
#     if rootnode is None:
#         return False
#     # if rootnode is the target itself
#     if rootnode.val == target:
#         return True
#     # logical OR operator, if any recursive call returns True, main function returns True.
#     return treeIncludesRecursive(rootnode.left, target) or treeIncludesRecursive(
#         rootnode.right, target
#     )


# print(f'Depth first traversal search (recursive): {treeIncludesRecursive(a, "f")}')
## True


# # ____________________________________________________________
# # TREESUM ( ADDING ALL ELEMENTS TOGETHER )

# # depthfirstTraversalrecuvrsive treesum
# # video time: 1:12:45
# # UNCOMMENT LINES 174 - 183


# def treesumdepthrecursion(rootnode):
#     if rootnode == None:
#         return 0
#     return (
#         rootnode.val
#         + treesumdepthrecursion(rootnode.left)
#         + treesumdepthrecursion(rootnode.right)
#     )

# print(f"Treesum Depth First Recursion: {treesumdepthrecursion(numA)}")


# Breadth First Tree Sum (iterative)
# video time: 1:15:46
# UNCOMMENT LINES 192-207

# # append and pop(0) work on the opposite ends of the list: exactly like a queue, which makes the breadth-first possible.

# def treesumiterative(rootnode):
#     if rootnode is None:
#         return 0
#     totalSum = 0
#     queue = [rootnode]
#     while len(queue) > 0:
#         current = queue.pop(0)
#         totalSum += current.val
#         if current.left:
#             queue.append(current.left)
#         if current.right:
#             queue.append(current.right)
#     return totalSum


# print(f"Breadth First Iterative Tree Sum: {treesumiterative(numA)}")


# #____________________________________________________________
# # TREE MIN VALUE


# # iterative DEPTH FIRST TIMESTAMP 1:26:00
# # UNCOMMENT LINES 216 - 230
# def treeMinValueStack(root):
#     smallest = float("inf")
#     stack = [root]
#     while len(stack) > 0:
#         current = stack.pop()
#         if current.val < smallest:
#             smallest = current.val
#         if current.left:
#             stack.append(current.left)
#         if current.right:
#             stack.append(current.right)
#     return smallest


# print(f"Tree Min Value Stack (Depth First): {treeMinValueStack(numA)}")

# # TREE MIN VALUE BREADTH FIRST (QUEUE) (POP FIRST VALUE OFF)
# # VIDEO TIME: 1:28:50
# # UNCOMMENT LINES 235 - 249
# def treeMinValueQueue(root):
#     smallest = float("inf")
#     queue = [root]
#     while len(queue) > 0:
#         current = queue.pop(0)
#         if current.val < smallest:
#             smallest = current.val
#         if current.left:
#             queue.append(current.left)
#         if current.right:
#             queue.append(current.right)
#     return smallest


# print(f"Tree Min Value Queue (Breadth First): {treeMinValueQueue(numA)}")


# # recursion (depth first) treeMinValue
# # VIDEO TIME 1:31:22
# # UNCOMMENT LINES 257 - 265
# # return inf if no value, else recursively find min from root.left and root.right, and it extends root to the left and right child recursively

# def treeMinValueRecursion(root):
#     if root is None:
#         return float("inf")
#     return min(
#         treeMinValueRecursion(root.left), root.val, treeMinValueRecursion(root.right)
#     )


# print(f"Tree Min Value Recursion (Depth first): {treeMinValueRecursion(numA)}")


# #____________________________________________________________
# MAX ROOT TO LEAF PATH SUM
# RECURSIVELY:BEST FOR PATH FINDING

# always ending at a leaf node, from parent node: no left and no right
# # VIDEO TIME 1:43:43
# # recursively
# # UNCOMMENT LINES 276 - 285
# def maxPathSum(root):
#     if root is None:
#         return float("-inf")
#     if root.left is None and root.right is None:
#         return root.val
#     max_child = max(maxPathSum(root.left), maxPathSum(root.right))
#     return root.val + max_child


# print(f"max path sum (recursively): {maxPathSum(numA)}")
