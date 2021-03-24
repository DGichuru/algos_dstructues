'''class Node:
    def __init__(self,val):
        self.childleft = None
        self.childright = None
        self.nodedata = val

root = Node(1)
root.childleft = Node(2)
root.childright = Node(3)
root.childleft.childleft = Node(4)
root.childleft.childright = Node(5)'''

##inorder traversal of a tree
'''def InOrd(root):
    if root:
        InOrd(root.childleft)
        print(root.nodedata)
        InOrd(root.childright)
InOrd(root)'''
##preorder traversal of a tree
'''def PreOrd(root):
    if root:
        print(root.nodedata)
        PreOrd(root.childleft)
        PreOrd(root.childright)
PreOrd(root)'''
##postorder traversal of a tree
'''def PostOrd(root):
    if root:
        PostOrd(root.childleft)
        PostOrd(root.childright)
        print(root.nodedata)
      
PostOrd(root)'''

#bubble sort algorithm
'''def bs(a):
    b = len(a)-1
    for x in range(b):
        for y in range(b-x):
            if a[y]>a[y+1]:
                a[y], a[y+1] = a[y+1],a[y]
    return a'''

#selection sort
def selsort(myarray, r):
    for x in range(r):
        minimum = x
        for y in range(x + 1, r):
            if myarray[y] < myarray[minimum]:
               minimum = y
        (myarray[x], myarray[minimum]) = (myarray[minimum], myarray[x]) 