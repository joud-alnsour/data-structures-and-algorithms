from hashmap_repeated_word.hashmap_repeated_word import hashmap_repeated_word

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

