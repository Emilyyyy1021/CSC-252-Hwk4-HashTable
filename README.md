Instructions
In this assignment you will build a working hash table data structure from scratch.
Your hash table class should consist of an array of singly linked lists, as described in the textbook. Then add appropriate methods to add/update, remove, and find items in the hash map. You will also write methods to calculate the load factor and rebuild the hash table in the event of a high-load factor. Finally, you will implement three hashing functions of your choice and compare (i.e., profile) them with each other, as well as the built in hash function in Python and no hash function. Real hash functions take in a string as a parameter; to make things easier for you, we assume that are hash keys are all integers. You are only allowed to use arrays and singly linked lists as data structures in this part. We provide hwk4.py as a starter file for your implementation and hwk4-people.csv which contains the data for your hash table.

Hash Table Class
Write the HashTable class with the following methods:

__init__(self, size:int, hash_choice:int) constructs a new empty hash table
__str__(self) -> str returns a human readable version of the contents of the hash table (programmers choice)
hashFunc(self, key:int) -> int a "private" function that calculates under which hash value you should store a given key depending on which of the five hash functions is being used (note: you may want to write/test this method last as a default hash function is already given)
insert(self, key:int, val:str) -> bool add a new key, value pair to the existing hash table and returns if the operation was successful (note: if the key already exists in your table, you should update it)
getValue(self, key:int) -> str returns the value given a key, or None if the key is not found
remove(self, key:int) -> bool removes a key, value pair from the hash table and returns if the operation was successful (note: if the key is not in the table, you should return False)
isOverLoadFactor(self) -> bool calculates the load factor for the current table and returns True if and only if it is greater than 0.7 (see textbook for details on calculating the load factor)
reHash(self) -> bool - creates a new hash table that is double the size of the current one and rehashes all of the key, value pairs into the new table
The testMain(), releaseMain(), and profileMain functions are given. You should use these functions to test, evaluate, and profile your code. You may edit or extend these function.

Hint: We strongly encourage you to create a separate singly linked list class to store your hashed elements, as discussed in the textbook.

Profiling
Once you have completed your HashTable class, you can profile the responsiveness of your hash table and hash functions in multiple scenarios. In the function hashFunc(self, key:int) -> int you created three additional hashing functions. As shown below, the default hash (0) and a single hash (1) are given:

  if self.hash_choice == 0:
      return hash(key) % self.size    #Embedded Python hash function.
  elif self.hash_choice == 1:
      return 0    #Everything in the has ia stored in a single linked list.   
You will compare each of these functions with the three additional ones you made. Our hypothesis is the embedded function should be the best and no (or single) hash function should be the worst.

You will extend the provided profilerMain() function to profile your code. To profile a piece of code you need to check the time, run just the code you want to check, then check the time again. The difference in time between the start and stop is how long it took your code to execute. Do not add any print statements in between the start and end time checks, it will throw off your times. For example, the given code calculates the time for one new insert into the hash table.

  print("Hash Map", i, "Initialized")
  start_time_create = time.time()    # Get start Time.
  #### Start of code you want to profile ####

  # Add/Edit code to profile
  row = csv_reader.__next__() 
  hash_table.insert(int(row[0]),row[1])

  #### End of code you want to profile ####
  end_time_create = time.time()      # Get end Time. 
  calc = end_time_create - start_time_create  
  print("Hash Map", i, "Test \tTime:", calc, "seconds.")
We've put the above code into a loop so that you can automatically time all 5 hash functions.

To run the profilerMain() instead of main() swap the commented out lines of code as shown below (which are located at the bottom of the file):

if __name__ == "__main__":
    # Swap these options to profile or test your code.
    profilerMain()   
    #main()
Expectations for Profiling: In a separate document (called hwk4-analysis), you should write up the results of your profiling. This part is open-ended on purpose. Part of this assignment is thinking through which parts of the hash table are most interesting to profile, isolating those parts, collecting data, and analyzing the difference. Some things to consider are the current load factor, individual operations (e.g., add, remove, get), and the hash function itself. Thus, you will not be graded on the final contents of profilerMain(), though you can leave intermediate steps as comments in your profilerMain() function.

In hwk4-analysis, write up your results similar to a lab report from a science class (max 3 pages):

What experiments did you try (you should do more than one)?
What were your expectations or hypotheses?
What results did you achieve (give actual data either in a table or directly from the terminal)?
How do you interpret the results?
What recommendations do you have for hash table developers?
