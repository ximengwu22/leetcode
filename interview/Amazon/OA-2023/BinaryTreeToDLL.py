# flake8: noqa
class Node:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# In-order traversal
class Solution:
    prevNode = None
    head = None
    
    def _binaryTreeToDll(self, root):
        if not root: return
        self._binaryTreeToDll(root.left)
        if not self.prevNode:
            self.head = root
        else:
            root.left = self.prevNode
            self.prevNode.right = root
        self.prevNode = root
        self._binaryTreeToDll(root.right)
    
    def binaryTreeToDll(self, root) -> Node:
        self.prevNode = None
        self._binaryTreeToDll(root)
        print(self.head)
        return self.head
    

def print_dll(head: Node):
    while head:
        print(head.val, end=" ")
        head = head.right
        

if __name__ == '__main__':
    root = Node(
        10,
        Node(12, Node(25), Node(30)),
        Node(15, Node(36))
    )
    sol = Solution()
    new_dll = sol.binaryTreeToDll(root)
    print_dll(new_dll)