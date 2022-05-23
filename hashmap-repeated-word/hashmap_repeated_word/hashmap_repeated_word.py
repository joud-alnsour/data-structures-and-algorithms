class Hashtable:
    def __init__(self, size=1024):
        self.size = size
        self.buckets = [[] for _ in range(self.size)]
    def hash(self, key):
        sum = 0
        for char in key:
            sum += ord(char)
        primed = sum * 521
        return  primed % self.size
    def set(self, key, value):
       
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

        index = self.hash(key)
        for record in self.buckets[index]:
            if record[0] == key:
                return record[1]
    def contains(self, key):
        index = self.hash(key)
        for record in self.buckets[index]:
            if record[0] == key:
                return True
        return False
    def keys(self):
        for record in self.buckets:
            return print(record)

def hashmap_repeated_word(text):
    '''
    Finds the first word to occur more than once in a string
    Arguments: string
    Return: string
    '''
    word_accumulator = ""
    hashmap = Hashtable()
    for char in text:
        lower_char = char.lower()
        if ord(lower_char) in range(ord("a"), ord("z")+1):
            word_accumulator += lower_char
        elif len(word_accumulator):
                if hashmap.contains(word_accumulator):
                    return word_accumulator
                else:
                    hashmap.set(word_accumulator, None)
                    word_accumulator = ""
    if len(word_accumulator) and hashmap.contains(word_accumulator):
        return word_accumulator
    return None

if __name__ == '__main__':
    text1 = "Once upon a time, there was a brave princess who..."
    print(hashmap_repeated_word(text1))
    text2 = "It was the best of times, it was the worst of times, it was the age of wisdom, it was the age of foolishness, it was the epoch of belief, it was the epoch of incredulity, it was the season of Light, it was the season of Darkness, it was the spring of hope, it was the winter of despair, we had everything before us, we had nothing before us, we were all going direct to Heaven, we were all going direct the other way – in short, the period was so far like the present period, that some of its noisiest authorities insisted on its being received, for good or for evil, in the superlative degree of comparison only..."
    print(hashmap_repeated_word(text2))
    text3 = "It was a queer, sultry summer, the summer they electrocuted the Rosenbergs, and I didn’t know what I was doing in New York..."
    print(hashmap_repeated_word(text3))
   

