#1.定义链表的基本元素：节点Node
class Node(object):
    '''
    data 保存节点的数据
    next 保存下一个节点的对象
    '''
    def __init__(self, data=None, pnext=None):
        self.data = data
        self.pnext = pnext
    
    def __repr__(self):
        '''
        用来定义 Node 的字符输出，
        print为输出data
        '''
        return str(self.data)

#2.把node连接起来
# （1）定义一个个的节点
node1 = Node(1)
node2 = Node(2)
node3 = Node(3)
# （2）表示出节点间的关系
node1.pnext = node2
node2.pnext = node3

#3.打印链表
# (1)顺序打印
def printlist(node):
    while node:
        print(node)
        node = node.pnext
# printlist(node1)
# (2)逆序打印
def backwardprintlist(node):
    if node == None:
        return 
    backwardprintlist(node.pnext)
    print(node)
# backwardprintlist(node1)

#4. 创建一个单链表&链表的基本操作
class Slinkedlist(object):
    def __init__(self):
        self.headval = None
    
    def append(self, newdata):
        '''
        在链表的末尾添加一个新的node
        '''
        newnode = Node(newdata)
        if self.headval is None:
            self.headval = newnode
            return 
        # 只有遍历一遍才能找到最后一个元素
        laste = self.headval
        while laste.pnext:
            laste = laste.pnext
        laste.pnext = newnode

    def forwardprint(self):
        '''顺序打印单链表'''
        printval = self.headval
        while printval:
            print(printval)
            printval = printval.pnext
    
    def backwardprint(self, node):
        '''逆序打印单链表'''
        if self.headval == None: return
        printval = node
        if printval == None: return
        self.backwardprint(printval.pnext)
        print(printval)

    def add_left(self, newdata_in):
        '''在链表的开头插入一个node'''
        newdata_in = Node(newdata_in)
        newdata_in.pnext = self.headval
        self.headval = newdata_in
    
    def insert(self, selected_node, newdata_in):
        '''在链表的两个元素之间插一个元素'''
        if not selected_node:
            print('error: the node methioned does not exsist')
        newnode_in = Node(newdata_in)
        newnode_in.pnext = selected_node.pnext
        selected_node.pnext = newnode_in
    
    def delete(self, removekey):
        '''删除指定位置的node'''
        if removekey is None: 
            return 
        if self.headval is None:
            print('The single list is empty!')
            return 
        if self.headval.data == removekey:
            self.headval = self.headval.pnext
            return
        pre_node = self.headval
        cur_node = self.headval.pnext
        while cur_node is not None:
            if cur_node.data == removekey:
                pre_node.pnext = cur_node.pnext
                return 
            else:
                pre_node = cur_node
                cur_node = cur_node.pnext
                
# test
l = Slinkedlist()
for i in range(6):
    l.append(i)
l.add_left(7)
l.insert(l.headval.pnext.pnext, 'haha')
# l.forwardprint()
# l.backwardprint(l.headval)
l.delete(5)
l.forwardprint()

