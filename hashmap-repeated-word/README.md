# Challenge Summary
Create a function called repeated word that finds the first word in a string that appears more than once. Strings as arguments string as output
## Whiteboard Process
![pic](/hashmap-repeated-word/assets/hashmap.jpg)
## Approach & Efficiency
**Big O**<br>
time:O(1)<br>
space:O(n)<br> 
## Solution
***Code***
```
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
```
***Test***  
```
def test_hashmap_word1():
    text1 = "Once upon a time, there was a brave princess who..."
    actual = hashmap_repeated_word(text1)
    expected = "a"
    assert actual == expected

def test_hashmap_word2():
    text2 = "It was the best of times, it was the worst of times, it was the age of wisdom, it was the age of foolishness, it was the epoch of belief, it was the epoch of incredulity, it was the season of Light, it was the season of Darkness, it was the spring of hope, it was the winter of despair, we had everything before us, we had nothing before us, we were all going direct to Heaven, we were all going direct the other way – in short, the period was so far like the present period, that some of its noisiest authorities insisted on its being received, for good or for evil, in the superlative degree of comparison only..."
    actual = hashmap_repeated_word(text2)
    expected = "it"
    assert actual == expected

def test_hashmap_word3():
    text3 = "It was a queer, sultry summer, the summer they electrocuted the Rosenbergs, and I didn’t know what I was doing in New York..."
    actual = hashmap_repeated_word(text3)
    expected = "summer"
    assert actual == expected
```
- [x] done README file   
- [x] done Whiteboard
- [x] done the test 
- [x] done the code 