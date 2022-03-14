class Node:


    def __init__(self,value):
        self.value = value
        self.next = None


class LinkedList:


    def __init__(self):
        self.head = None

    

    def insert(self,value):
        
          
        if value == '':
            raise TypeError('empty value')
        else:
            #value = Node(value)
            value.next = self.head
            self.head = value
         

    def includes(self,value):
        if value is None:
            raise TypeError('empty value')
        else:    
            current = self.head
            while current:
                if current.value == value:
                    return True
                current = current.next
            return False


    def __str__(self):
            message = ""
            if self.head is None:
                message = "Linked list is Null"
            else:
                current = self.head
                while current is not None:
                    message += f'{current.value} ->'
                    current = current.next
                message += "NULL"
            return message

            
    def to_string(self):
        return self.__str__()
            
     
if __name__ == '__main__':
   ll=LinkedList()
   ll.head=Node('joud')
   ll.x=Node('good')
   ll.insert(Node(True)) 
   print(ll.includes('joud'))
   print(ll)
  
