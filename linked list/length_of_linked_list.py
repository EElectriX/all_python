class Node:
  def __init__(self, data1, next1=None):
     self.data= data1
     self.next=next1

def print_linked_list(head):
  count = 0
  while head is not None:
    count+=1
    print(f"{head.data}",end=",")
    head=head.next
  print ("\n")
  print(f"The length of the linked list is :{count}") 

if __name__=="__main__":
  list= [5,10,15,20]
  value= 25
  value2= 30
   
  head=Node(list[0])
  head.next=Node(list[1])
  head.next.next=Node(list[2])
  head.next.next.next=Node(list[3])

  print (f"data: ", end="")

  print_linked_list(head)
  
