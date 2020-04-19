class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
        self.prev=None
class DLL:
    def __init__(self):
        self.head=None
        self.tail=None
    def containswith(self,node):
        cur=self.head
        while cur is not None and cur.value!=node:
            cur=cur.next
        return cur is not None
    def sethead(self,nodetoinsert):
        if self.head is None:
            self.head=nodetoinsert
            self.tail=nodetoinsert
            return
        self.insertbefore(self.head,nodetoinsert)
    def settail(self,nodetoinsert):
        if self.tail is None:
            self.sethead(nodetoinsert)
            return
        self.insertafter(self.tail,nodetoinsert)
    def insertbefore(self,node,nodetoinsert):
        if nodetoinsert==self.head and nodetoinsert==self.tail:
            return
        self.remove(nodetoinsert)
        nodetoinsert.prev=node.prev
        nodetoinsert.next=node
        if node.prev is not None:
            node.prev.next=nodetoinsert
        else:
            self.head=nodetoinsert
        node.prev=nodetoinsert
    def insertafter(self,node,nodetoinsert):
        if nodetoinsert==self.head and nodetoinsert ==self.tail:
            return
        self.remove(nodetoinsert)
        nodetoinsert.next=node.next
        nodetoinsert.prev=node
        if node.next is not None:
            node.next.prev=nodetoinsert
        else:
            self.tail=nodetoinsert
        node.next=nodetoinsert
    def removewithvalues(self,node):
        cur=self.head
        while cur is not None:
            temp=cur
            cur=cur.next
            if temp.data==node.data:
                self.remove(temp)
    def remove(self,node):
        if node==self.head:
            self.head=self.head.next
        if node==self.tail:
            self.tail=self.tail.prev
        self.removebindings(node)
    def removebindings(self,node):
        if node.prev is not None:
            node.prev.next=node.next
        if node.next is not None:
            node.next.prev=node.prev
        node.next=None
        node.prev=None
    def takeall(self):
        cur=self.head
        if cur is None:
            return
        a=[]
        while cur is not None:
            a.append(cur.data)
            cur=cur.next
        return a
            
