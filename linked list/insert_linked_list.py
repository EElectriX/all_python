class Node:
  def __init__(self, data1, next1=None):
     self.data= data1
     self.next=next1

def print_linked_list(head):
    while head is not None:
        print(f"{head.data}",end=",")
        head=head.next
    print ("\n") 

def create_node(value,head):
      temp= Node(value,head)
      return temp 

def insert_last(input,last):
   last_node= Node(input)
   last.next=last_node
   return last_node 

if __name__=="__main__":
   list= [5,10,15,20]
   value= 25
   value2= 30
   
   #head=Node(list[0])
   #head.next=Node(list[1])
   #head.next.next=Node(list[2])
   #head.next.next.next=Node(list[3])

   node0=Node(list[0])
   node1=Node(list[1])
   node2=Node(list[2])
   node3=Node(list[3])
   
   head=node0 
   node0.next=node1 
   node1.next=node2
   node2.next=node3
   last=node3
 
  

   print (f"data before insert: ", end="")

   print_linked_list(head)

   head= create_node(value,head)

   print (f"data after insert: ", end="")

   print_linked_list(head)
   
   last = insert_last(value2,last)

   print (f"data insert at last: ", end="")

   print_linked_list(head)


   
    
