


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
            value = Node(value)
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


    # def append(self,value):
    #     if value == '':
    #         raise TypeError('Node not empty')
    #     else:
            
    #         if self.head is None:
    #             self.head = value
            
    #         else:
    #             current = self.head
    #             while current.next :
    #                 current = current.next
    #             current.next = value   


    def insert_after(self, old , new):
      
        if new == None:
            raise TypeError('value is empty')
        if old == None:
            raise TypeError('value is empty')
        else:
            old = Node(old)
            new = Node(new)
            current =  self.head
        while current:
            if current.value == old.value:
                new.next = current.next
                current.next = new
            current = current.next
        return

       

    def insert_befor(self, value , new):
        value = Node(value)
        new = Node(new)
        if self.head == None:
            return

        if self.head.value == value:
            return

        current =  self.head
        if current.value== value:
            new.next= current
            self.head=new
        while current:
            if current.next.value == value.value: 
                new.next= current.next
                current.next = new    
                return 
            current = current.next    
            
                


    def get_kth_from_end(self,k):
        extent = 0
        current=self.head
        if k<0:
             raise Exception ('the index must be positive')
        while current:
            current = current.next 
            extent = extent + 1 
        if extent <= k:
            raise Exception ('The index is out of bounds')
        else: 
            current=self.head
        for i in range(extent - (k+1)):
            current = current.next
        print(current.value)
        return current.value





if __name__ == '__main__':
   ll=LinkedList()
   ll.head=Node('joud')
   ll.insert('tala')
   ll.insert('language')        
   ll.insert('best')
   ll.insert('is')
 
#    ll.x=Node('good')
#    ll.insert(Node(True)) 
#    ll.insert_after('add' , 'nice')
#    ll.insert_befor('python' , 'language')
#    print(ll.includes('joud'))
#    ll = ll.__str__()
   ll.get_kth_from_end(0)
   print(ll)
  
