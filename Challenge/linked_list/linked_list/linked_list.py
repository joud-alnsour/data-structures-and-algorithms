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

    def append(self,value):
        if value == '':
            raise TypeError('Node not empty')
        else:
            
            if self.head is None:
                self.head = value
            
            else:
                current = self.head
                while current.next is not None:
                    current = current.next
                current.next = value   


    def insert_after(self, value , new):

        if self.head == None:
            return

        current =  self.head
        while current:
            if current.value == value:
                current.next=Node(new , current.next)
            current = current.next
        return

       

    def insert_befor(self, value , new):
         
        if self.head == None:
            return

        if self.head.value == value:
            self.insert_at_beginning()
            return

        current =  self.head
        while current:
            if self.head == None:
                break

            if current.next.value == value: 
                node = Node(new , current.next)
                node.next= current.next
                current.next = node    
                return
            else:
                return (-1)



if __name__ == '__main__':
   ll=LinkedList()
   ll.head=Node('joud')
   ll.x=Node('good')
   ll.insert(Node(True)) 
   ll.insert_after('add' , 'nice')
   ll.insert_befor('python' , 'language')
   print(ll.includes('joud'))
   #ll = ll.__str__()
   print(ll)
  
