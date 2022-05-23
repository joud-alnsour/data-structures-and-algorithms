# Hashtables
Create a Hashtable with 5 internal functions to implement that hashtable
## Challenge
Create a hashtable class that will be able to hash, set a key value pair, return a value based on the key, check if the table contains the key, and return all the current keys within the hash tablee.
## Approach & Efficiency
Implemented a HashTable class with a list of None values. Items are added to the hash storage as lists. Collisions are appended to the bucketed list.
Big O<br>
Time: O(1)<br>
Space: O(n) 
## API
- Init : Creates the hashtable with a self.size and self.buckets the self.size is your current size of the hashtable and the buckets is how many buckets you create based on that sized
- Hash: Will take a key and then return the index by taking each char in the key and and getting its ascii value then multiplying that by 521 then return that new primed number % by the size of the current hashtable
- Set: This method will use the above hash method to hash a given key then it will add the new key and value pair to the current hashtable if something already exist at that index it will then handle that collision by appending the new key value pair on to the existing one
- Get: Will take in a key and then return the matching key value pair from the hashtable
- Contains: Will take in a key and search through the hashtable a return a boolean of true if it is within the table and false if it is not
- Keys: Will return all the keys stored within the Hashtable.
