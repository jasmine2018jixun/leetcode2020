'''树的构建：
                10
           6         14
        4    8    12    16
'''
class Node(object):
    '''节点类'''
    def __init__(self, elem=-1, lchild=None, rchild=None):
        self.elem = elem
        self.lchild = lchild
        self.rchild = rchild

class Tree(object):
    '''树类'''
    def __init__(self):
        self.root = Node()
        self.mq = []
        self.res_preorder = []
        self.res_inorder = []
        self.res_postorder = []

    def add(self, elem):
        '''为树添加节点'''
        node = Node(elem)
        if self.root.elem == -1:#如果树是空的，对根节点赋值
            self.root = node
            self.mq.append(self.root)
        else:
            treenode = self.mq[0]
            if treenode.lchild is None:
                treenode.lchild = node
                self.mq.append(treenode.lchild)
            else:
                treenode.rchild = node
                self.mq.append(treenode.rchild)
                self.mq.pop(0) #如果该结点存在右子结点，则将根节点丢弃
    def preorder_traversal(self, root):
        '''
        前序遍历：递归实现
        先访问根节点，再访问左子节点，最后访问右子节点
        '''
        if root is None:
            return 
        self.res_preorder.append(root.elem)
        self.preorder_traversal(root.lchild)
        self.preorder_traversal(root.rchild)

    def inorder_traversal(self, root):
        '''
        中序遍历：递归实现
        先访问左子节点，再访问根节点，最后访问右子节点
        '''
        if root is None:
            return 
        self.inorder_traversal(root.lchild)
        self.res_inorder.append(root.elem)
        self.inorder_traversal(root.rchild)
    def postorder_traversal(self, root):
        '''
        后序遍历：递归实现
        先访问左子节点，再访问右子节点，最后访问根节点
        '''
        if root is None:
            return 
        self.postorder_traversal(root.lchild)
        self.postorder_traversal(root.rchild)
        self.res_postorder.append(root.elem)

    def preorder_traversal1(self, root):
        '''
        前序遍历：栈实现
        先访问根节点，再访问左子节点，最后访问右子节点
        '''
        if root is None:
            return 
        mystack = []#用栈实现后进先出，弹出最近一个没有左子树的节点
        node = root
        while node or mystack:
            while node: # 从根节点开始，一直寻找它的左子树
                print(node.elem)
                mystack.append(node)
                node = node.lchild
            node = mystack.pop()
            node = node.rchild

    def inorder_traversal1(self, root):
        '''
        中序遍历：栈实现
        先访问左子节点，再访问根节点，最后访问右子节点
        '''
        if root is None:
            return 
        mystack = []#用栈实现后进先出，弹出最近一个没有左子树的节点
        node = root
        while node or mystack:
            while node: # 从根节点开始，一直寻找它的左子树
                mystack.append(node)
                node = node.lchild
            node = mystack.pop()
            print(node.elem)
            node = node.rchild

    def postorder_traversal1(self, root):
        '''
        后序遍历：栈实现
        先访问左子节点，再访问右子节点，最后访问根节点
        '''
        if root is None:
            return 
        mystack1 = []
        mystack2 = []
        mystack1.append(root)
        while mystack1:
            node = mystack1.pop()
            if node.lchild:
                mystack1.append(node.lchild)
            if node.rchild:
                mystack1.append(node.rchild)
            mystack2.append(node)
        while mystack2:
            print(mystack2.pop().elem)

    # 宽度优先遍历
    def BFS(self,root):              
        if root is None:
            return
        queue = []
        queue.append(root)
        while queue:
            now_node = queue.pop(0)
            print(now_node.elem)
            if now_node.lchild:
                queue.append(now_node.lchild)
            if now_node.rchild:
                queue.append(now_node.rchild)

        


if __name__ == '__main__':
    elems = [10, 6, 14, 4, 8, 12, 16]
    tree = Tree()
    for elem in elems:
        tree.add(elem)
    # tree.preorder_traversal(tree.root)
    # tree.inorder_traversal(tree.root)
    # tree.postorder_traversal(tree.root)
    # print('preorder')
    # print(tree.res_preorder)
    # print('inorder')
    # print(tree.res_inorder)
    # print('postorder')
    # print(tree.res_postorder)
    # tree.preorder_traversal1(tree.root)
    # tree.inorder_traversal1(tree.root)
    # tree.postorder_traversal1(tree.root)
    tree.BFS(tree.root)






        
