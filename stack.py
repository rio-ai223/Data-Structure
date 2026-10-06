#from loan_payment import LoanPayment
#from savings_account import SavingsAccounts
from priority_node import PriorityNode

class Stack:
  def __init__(self):
    self.head = None
    self.size = 0

  def push(self, value):
    new_prioritynode = PriorityNode(value)
    if self.head:
      new_prioritynode.next = self.head
    self.head = new_prioritynode
    self.size += 1

  def pop(self):
    if self.isEmpty():
      return "Stack is empty"
    popped_node = self.head
    self.head = self.head.next
    self.size -= 1
    return popped_node.value

  def peek(self):
    if self.isEmpty():
      return "Stack is empty"
    return self.head.value

  def isEmpty(self):
    return self.size == 0

  def stackSize(self):
    return self.size

 # def traverseAndPrint(self):
  #  currentNode = self.head
   # while currentNode:
    #  print(currentNode.value, end=" -> ")
     # currentNode = currentNode.next
    #print()
