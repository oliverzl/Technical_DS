
class Node:
    def __init__(self, val):
        self.val = val
        self.right = None
        self.left = None


a = Node('a')
b = Node('b')
c = Node('c')
d = Node('d')
e = Node('e')
f = Node('f')

a.left = b
a.right = c
b.left = d
b.right = e
c.right = f


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




#____________________________________________________________
# DEPTH FIRST SEARCH 

# #ITERATIVE
# def depthFirstValues(rootnode):
#     if rootnode is None:
#         return []
#     result = []
#     stack = [rootnode]
#     while len(stack) > 0:
#         current = stack.pop()
#         result.append(current.val)
#         if current.right:
#             stack.append(current.right)
#         if current.left:
#             stack.append(current.left)
#     return result

# print(depthFirstValues(a))


# # RECURSIION USING STACK
# def  depthFirstRecursion(rootnode):
#     if rootnode is None:
#         return []
#     leftValues = depthFirstRecursion(rootnode.left) # [b, d, e]
#     rightValues = depthFirstRecursion(rootnode.right) # [c, f]
#     # *leftvalues unpacks the array of values. 
#     return [rootnode.val, *leftValues, *rightValues]

# print(depthFirstRecursion(a))


# # BREADTH FIRST SEARCH 
# # no recursion because breadth first uses a queue

# def breadthFirstValues(rootnode):
#     if rootnode == None:
#         return []
#     values = []
#     queue = [rootnode]
#     while len(queue) > 0:
#         current = queue.pop()
#         values.append(current.val)
#         if current.left is not None:
#             queue.append(current.left)
#         if current.right is not None:
#             queue.append(current.right)
#     return values
        
# print(breadthFirstValues(a))  



#   ____________________________________________________________
# # TREE INCLUDES
# # breadth first traversal tree includes, iterative
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

# print(treeIncludesBreadth(a, 'f'))


# #------------------------------------------
# # depth first tree includes recursive

# def treeIncludesRecursive(rootnode, target):
#     if rootnode is None:
#         return False
#     # if rootnode is the target itself
#     if rootnode == target:
#         return True
#     # logical OR operator, if any recursive call returns True, main function returns True.
#     return treeIncludesRecursive(rootnode.left, target) or treeIncludesRecursive(rootnode.right, target)




# # ____________________________________________________________
# # TREESUM

# # depthfirstTraversalrecuvrsive treesum

# def treesum(rootnode):
#     if rootnode is None:
#         return 0
#     return treesum(rootnode.left) + rootnode.val + treesum(rootnode.right)
    
# print(treesum(numA))


# # breadthfirsttreesum
# # append and pop(0) work on the opposite ends of the list: exactly like a queue, which makes the breadth-first possible. 
# def treesumbreadth(rootnode):
#     if rootnode is None:
#         return 0
#     total_sum = 0
#     queue = [ rootnode ]
#     while len(queue) > 0:
#         current = queue.pop(0)
#         if current.left:
#             queue.append(current.left)
#         if current.right:
#             queue.append(current.right)
#         total_sum += current.val
#     return total_sum

# print(treesumbreadth(numA))


# #____________________________________________________________
# # timestamp 1:19:59 treeMinValue

# # iterative TIMESTAMP 1:29:19
# def treeMinValueIterative(root):
#     smallest = float('inf')
#     stack = [ root ]
#     while len(stack) > 0:
#         current = stack.pop(0)
#         if current.val < smallest:
#             smallest = current.val
#         if current.left:
#             stack.append(current.left)
#         if current.right:
#             stack.append(current.right)
#     return smallest

# # testing treeMinValueIterative
# print(treeMinValueIterative(numA))


        
# # recursion treeMinValue
# def treeMinValueRecursion(root):
#     if root is None:
#         return float('inf')
#     return min(treeMinValueRecursion(root.left), root.val, treeMinValueRecursion(root.right))


# print(treeMinValueRecursion(numA))


# #____________________________________________________________
# # MAX ROOT TO LEAF PATH SUM
# # RECURSIVELY:BEST FOR PATH FINDING

# # always ending at a leaf node, from parent node: no left and no right

# # # recursively 
# def maxPathSum(root):
#     if root is None:
#         return float("-inf")
#     if root.left is None and root.right is None:
#         return root.val
#     max_child = max(maxPathSum(root.left), maxPathSum(root.right))
#     return root.val + max_child

# print(maxPathSum(numA))

