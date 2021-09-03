Q = int(input())

qs = []
for i in range(Q):
    qs.append([int(k) for k in input().split(" ")])

class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key
        self.add = 0
 
def insert(root, key):
    if root is None:
        return Node(key)
    else:
        root.val += root.add   
        add_n(root.right,root.add)
        add_n(root.left,root.add)
        if root.val < key:
            root.right = insert(root.right, key)
        else:
            root.left = insert(root.left, key)
    root.add = 0
    return root
 
def inorder(root):
    if root:
        inorder(root.left)
        print(root.val)
        inorder(root.right)

def add_n(root, n):
    if not (root is None):
        root.add += n

def delete_min(root):
    a = root.add
    root.val += a
    add_n(root.right,root.add)
    add_n(root.left,root.add)
    root.add = 0
    if root.left is None:
        m = root.val
        root = root.right
    elif not(root.left.left is None):
        delete_min(root.left)
    else:
        m = root.left.left.val+a
        if root.left.right is None:
            root.left.left = None
        else:
            root.left =root.left.right

    return m

r = None
for qsi in qs:
    if (len(qsi) == 1) and r!=None:  
        print(delete_min(r))
        # inorder(r)
    else:
        if (len(qsi) == 2) and (qsi[0]==1) and (r==None):
            r = Node(qsi[1])
        elif  (len(qsi) == 2) and (qsi[0]==1) and (r!=None):
            insert(r, qsi[1])
        elif  (len(qsi) == 2) and (qsi[0]==2) and (r!=None):
            add_n(r, qsi[1])
        
