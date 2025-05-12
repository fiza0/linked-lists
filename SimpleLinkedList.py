class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

class LinkedList:
    def __init__(self):
        self.head = None

    def InsertAtBeginning(self,new_data):
        new_node = Node(new_data)
        new_node.next=self.head
        self.head=new_node

    def print(self):
        temp=self.head
        while temp:
            print(f'{temp.data}',end=' ')
            temp=temp.next
        print()


if __name__=='__main__':
    Llist=LinkedList()

    Llist.InsertAtBeginning('New')
    Llist.InsertAtBeginning('Data')
    Llist.InsertAtBeginning('is')
    Llist.InsertAtBeginning('new')
    Llist.InsertAtBeginning('Data')

    Llist.print()

'''class LinkedListNode:
    def __init__(self,value,nextNode=None):
        self.value=value
        self.nextNode=nextNode

node1 = LinkedListNode('1')
node2 = LinkedListNode('2')
node3 = LinkedListNode('3')
node4 = LinkedListNode('4')
node5 = LinkedListNode('5')
node6 = LinkedListNode('6')


node1.nextNode=node2
node2.nextNode=node3
node3.nextNode=node4
node4.nextNode=node5
node5.nextNode=node6

currentNode=node1

while True:
    print(currentNode.value,">>> ",end=' ')
    if currentNode.nextNode==None:
        print('None')
        break
    currentNode=currentNode.nextNode'''

