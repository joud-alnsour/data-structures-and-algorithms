class Hashtable(object):
    def __init__(self, size=1024):
        self.size = size
        self.table = [None] * size
 
    def hash(self, key):
       
        if type(key) is not str:
            raise Exception("Key must be a string")
        sum_of_ascii = 0
        for ch in key:
            ch_ascii = ord(ch)  
            sum_of_ascii += ch_ascii
        hashed_key = (sum_of_ascii * 19) % self.size
        return hashed_key

    def set(self, key, value):
        
        if type(key) is not str and type(value) is not str:
            raise Exception("Key and Value must be strings")
        idx = self.hash(key)
        if not self.table[idx]:
            self.table[idx] = [[key, value]] 
        else:
            self.table[idx].append([key, value])

    def get(self, key):
       
        if type(key) is not str:
            raise Exception("Key must be a string")
        index = self.hash(key)
        if not self.table[index]:
            return None
        for arr in self.table[index]:
            if arr[0] == key:
                return arr[1]

    def keys(self):
          
        keys = []
        for bucket in self.table:
            if bucket is not None:
                for arr in bucket:
                    keys.append(arr[0])
        return keys



    def contains(self, key):
         
        if type(key) is not str:
            raise Exception("Key must be a string")
        if self.get(key):
            return True
        else:
            return False

    def __str__(self):
        output = ""
        for bucket in self.table:
            if bucket is not None:
                output += f"{bucket} \n"
        return output


def left_join_hash(hashmap1, hashmap2):
  try:
    hashmap3 = Hashtable()

    for key in hashmap1.keys():        
        if hashmap2.contains(key):
            hashmap3.set(key, [hashmap1.get(key), hashmap2.get(key)])
        else:
            hashmap3.set(key, [hashmap1.get(key), 'Null'])
    return hashmap3
  except Exception:
        raise Exception("HashTable objects must be used for both hash tables.")

if __name__ == "__main__":
    hashmap1 = Hashtable()
    hashmap1.set('diligent', 'employed')
    hashmap1.set('fond', 'enamored')
    hashmap1.set('guide', 'usher')
    hashmap1.set('outfit', 'garb')
    hashmap1.set('wrath', 'anger')
    hashmap2 = Hashtable()
    hashmap2.set('diligent', 'idle') 
    hashmap2.set('fond', 'averse')
    hashmap2.set('guide', 'follow')
    hashmap2.set('flow', 'jam')
    hashmap2.set('wrath', 'delight')
    hashmap = left_join_hash(hashmap2, hashmap1)
    print(hashmap)
    