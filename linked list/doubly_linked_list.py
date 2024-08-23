class Node:
  def __init__(self,data , next_node=None, back_node=None):
    self.data=data
    self.next=next_node
    self.back=back_node

def convert(arr):
  head=Node(arr[0])
  prev=head
  for i in range(1,len(arr)):
    temp=Node(arr[i],None,prev)
    prev.next=temp
    prev=temp
  return head 

def print_node(head):
  tempo=head
  while tempo is not None:
    print(tempo.data,end=",")
    tempo=tempo.next
  print("\n")

def insert_node(value):
  temp=head
  while temp.next is not None:
    temp=temp.next
  new=Node(value,None,temp)
  temp.next=new
  return head

  


if __name__=="__main__":
  arr=[10,20,30,40,50]
  val=60
  head= convert(arr)
  print("the primary doubly linked list is :" , end="")
  print_node(head)
  head=insert_node(val)
  print("the doubly linked list after last insert is :" , end="")
  print_node(head)



   

