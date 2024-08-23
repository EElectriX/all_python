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
  
  print(f"The length of the linked list is :{count}") 

def convert(list):
  head=Node(list[0])
  construct=head
  for i in range(1,len(list)):
    temp=Node(list[i])
    construct.next=temp
    construct=temp
  return head

def delete_last(head):
  temp=head
  while temp.next.next is not None:
    temp=temp.next
  temp.next=None

def delete_start(head):
  head=head.next
  return head

def delete_twenty(head):
  temp= head
  while temp.next.data != 20:
    temp=temp.next
  temp.next=temp.next.next

def delete_index_four(head):
  temp= head
  count=0
  count_upto=4
  while count!= count_upto-1:
    temp=temp.next
    count+=1
  temp.next=temp.next.next


    

if __name__=="__main__":
  list= [5,10,15,20,30,35,40,45,50]

  head=convert(list)

  print (f"data: ", end="")

  print_linked_list(head)
  
  delete_last(head)

  print (f"delete last: ", end="")  
  print_linked_list(head)

  head= delete_start(head)

  print (f"delete start: ", end="")  
  print_linked_list(head)
  
  delete_twenty(head)

  print (f"delete 20: ", end="")  
  print_linked_list(head)


  delete_index_four(head)
  
  print (f"delete index 4: ", end="")  
  print_linked_list(head)

#   output:

# data: 5,10,15,20,30,35,40,45,50,The length of the linked list is :9
# delete last: 5,10,15,20,30,35,40,45,The length of the linked list is :8
# delete start: 10,15,20,30,35,40,45,The length of the linked list is :7
# delete 20: 10,15,30,35,40,45,The length of the linked list is :6
# delete index 4: 10,15,30,35,45,The length of the linked list is :5