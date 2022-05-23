class Hashtable:
    def __init__(self, size=1024):
        self.size = size
        self.buckets = [[] for _ in range(self.size)]
    def hash(self, key):
        # Arguments: key
        # Returns: Index in the collection for that key
        sum = 0
        for char in key:
            sum += ord(char)
        primed = sum * 521
        return  primed % self.size
    def set(self, key, value):
        # Arguments: key, value
        # Returns: nothing
        # This method should hash the key, and set the key and value pair in the table, handling collisions as needed.
        # Should a given key already exist, replace its value from the value argument given to this method.
       index = self.hash(key)
       key_found = False

       for i, record in enumerate(self.buckets[index]):
           if len(record) == 2 and record[0] == key:
               self.buckets[index][i] = (key, value)
               key_found = True
               break

       if not key_found:
           self.buckets[index].append((key,value))

    def get(self, key):
        # Arguments: key
        # Returns: Value associated with that key in the table
        index = self.hash(key)
        for record in self.buckets[index]:
            if record[0] == key:
                return record[1]
    def contains(self, key):
        # Arguments: key
        # Returns: Boolean, indicating if the key exists in the table already.
        index = self.hash(key)
        for record in self.buckets[index]:
            if record[0] == key:
                return True
        return False
    def keys(self):
        # Returns: Collection of keys
        for record in self.buckets:
            return print(record)
        # return print(self.buckets)


if __name__ == '__main__':
    table1 = Hashtable()
    print(table1.hash('dog'))
    table2 = Hashtable()
    table2.set('cat','Mouse')
    print(table2.contains('cat'))
    print(table2.contains('meat'))
