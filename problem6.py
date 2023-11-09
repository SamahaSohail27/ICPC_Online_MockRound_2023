class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def buildTree(inorder, postorder):
    if not inorder or not postorder:
        return None
    
    root_val = postorder.pop()
    root = TreeNode(root_val)
    inorder_index = inorder.index(root_val)
    
    root.right = buildTree(inorder[inorder_index + 1:], postorder)
    root.left = buildTree(inorder[:inorder_index], postorder)
    
    return root

def isPathExist(root, target_sum):
    if not root:
        return False
    
    if not root.left and not root.right:
        return target_sum == root.val
    
    target_sum -= root.val
    
    if isPathExist(root.left, target_sum) or isPathExist(root.right, target_sum):
        return True
    
    return target_sum == 0

def process_test_case():
    inorder = list(map(int, input().split()))
    postorder = list(map(int, input().split()))
    target_sums = list(map(int, input().split()))
    
    root = buildTree(inorder, postorder)
    
    for target_sum in target_sums:
        result = "TRUE" if isPathExist(root, target_sum) else "FALSE"
        print(result)

N = int(input())

for _ in range(N):
    process_test_case()
