# Name:  - Emily Wang & Tanya Chen
# Peers:  - names of CSC252 students who you consulted or ``N/A'' <br>
# References:  - https://www.datacamp.com/tutorial/python-linked-lists
#              - CSC210 Linked List Assignment
import math # pyright: ignore[reportUnusedImport]
import time
import csv          # Used to read a .csv file.

### DO NOT EDIT ###
def new_array(size: int):
    """ Creates a new array of a given size.
    :param size: (int) the number of 0s you want in the array
    :return : (list) the array with zeros 
    >>> new_array(3)
    [0,0,0]
    """
    L = [0] * size
    return L

class HashNode:
    """Class to instantiate linked list node objects, with both a key and a value.
    >>> node = HashNode(7, "Matt Damon")
    >>> print(node)
    {key:7, value:Matt Damon}
    """
    
    def __init__(self, key:int, value:str) -> None:
        """ Constructor of new node with a key and value. Initially nodes do not have a next value.
        :param key: (int) the key that will be added to the node
        :param value: (str) the value that will be added to the node
        :return : (HashNode) a pointer to the object
        """
        self.key = key
        self.value = value
        self.next: HashNode | None = None
        
    def __str__(self) -> str:
        """ Returns a string representation of the object.
        :return : (str) a string description of the HashNode object.
        """
        return "{key:" + str(self.key) + ", value:" + self.value + "}"     
### END OF DO NOT EDIT###

# Hint: create a linked list class here...
class LinkedList:
    def __init__(self):
        self.head:  HashNode | None = None
    
    def insertAtBeginning(self, key: int, value: str):
        node = HashNode(key, value)  # Create a new node 
        node.next = self.head  # Next for new node becomes the current head
        self.head = node  # Head now points to the new node

    def insertAfter(self, key: int, value: str):
        #I just feel like I want the new node to be at the end
        #it can be the first one, and it will be more efficient
        new_node = HashNode(key, value)  # Create a new node
        if self.head is None:
            self.head = new_node  # If the list is empty, make the new node the head
            return
        last = self.head 
        while last.next:  # Otherwise, traverse the list to find the last node
            last = last.next
        last.next = new_node  # Make the new node the next node of the last node

    def remove(self, key:int, value: str):
        """
        
        """
        # Question whether it works/we need it
        new_node = HashNode(key, value)
        
        if self.head is None:
            self.head = new_node
            return
        
        temp = self.head

        while temp.next != None:
            if temp.next.key == key:
                temp.next = temp.next.next
                
        # prev = self.head 
        # if prev.next is None:
        #     return None
        # current = prev.next
        # while current.next:  
        #     if current.key == key:
        #         prev = current.next
        #     current = current.next
        pass

class HashTable:
    def __init__(self, size:int, hash_choice:int) -> None:
        self.size = size
        self.hash_choice = hash_choice                  # Which hash function you will use.
        #TODO Finish constructor...
        self.array = new_array(size) 
        # self.array = [None] * size
        self.list = LinkedList() 
    
    def __str__(self) -> str:
        return "Hash Table"
        
    def hashFunc(self, key:int) -> int|None:
        if type(key) != int:
            return None
        if self.hash_choice == 0:
            return hash(key) % self.size    #Embedded Python hash function.
        elif self.hash_choice == 1:
            return 0    #Everything in the hash is stored in a single linked list.
        elif self.hash_choice == 2:
            # Module the given index with 5 and times the original key with its module
            mod = key%5
            revised_key = key*mod

            # Module the result with its size
            revised_key = revised_key%self.size
            return revised_key
            
        elif self.hash_choice == 3:
            pass #TODO Implement your has functions here.
        elif self.hash_choice == 4:
            pass #TODO Implement your has functions here.
        return None
    
    def insert(self, key:int, val:str) -> bool:
        index = self.hashFunc(key) #find index with hash function
        #print(index)
        if index is None: #no index
            return False
        # index exsists
        if self.array[index] == 0:
            self.array[index] = LinkedList() #type: ignore
        inside_list: LinkedList = self.array[index]  #type: ignore
        inside_list.insertAfter(key, val)

        return True 
    
    def getValue(self, key:int) -> str|None:
        """ Given key, get corresponding value if key is stored in hash table
        :param key: (int) 
        : return : (str|None) a string value that the key matches to or None because key DNE in hash table

        >>> value = getValue(1)
        >>> print(value)
        "3"
        """

        # Check whether key is in hash table by letting it passes through hash function
        index:int|None = HashTable.hashFunc(self,key)
        #print(index)
        # If DNE: return None
        if index == None:
            return None
        
        if index > len(self.array) or index < 0:
            return None
        
        if self.array[index] == 0:
            return None
        else:
            # If key exists: loop through the linked list to find the matching key and their value

            node = self.array[index].head #type:ignore

            while node.next is not None: #type:ignore
                if node.key == key: #type:ignore
                    return node.value #type:ignore
                node = node.next #type:ignore
            

    def remove(self, key:int) -> bool:
        # Rewrite the pseudo code a little
        # Return FALSE if
        #               1. there is nothing in array/hash table
        #               2. there is nothing (0) in the array of corresponding index
        # Return TRUE if we successfully removed value and key
        # 

        #If the key is not in the hash table, return false
        index = HashTable.hashFunc(self, key)

        if index == None:
            return False
        elif index > len(self.array) or index < 0:
            return False
        elif self.array[index] == 0:
            return False
        
        # Remove key value pair if key exists
        # Check whether the hash function is hashing 2 keys to the same index
        if key != self.array[index]:
            return False
        else:
            self.array[index] = 0
            return True
    
    def isOverLoadFactor(self) -> bool:
        """ Calculate the loaf factor of a hash table and check whether LF is greater than 0.7
        :return : (bool) whether the hash table is overloaded or not

        >>> overloaded = isOverLoadFactor()
        True
        """
        # Find filled blocks in array
        count = 0
        for i in range(len(self.array)):
            if self.array[i] != 0:
                count += 1

        # Calculate load factor using the equation: /total number
        load_factor = count/len(self.array)

        # Check whether the hash table is overloaded
        if load_factor >= 0.7:
            return True
        
        return False
    
    def reHash(self) -> bool:
        # Create an array with double original size
        # new_arr = new_array(2*self.size)
        
        # 
        return False

def testMain() -> None:            
    # Use this function to test your code as you develop, especially your singly-linked list. 
    # Review, but do not use, profileMain or releaseMain until you are well into development.
    hash_table = HashTable(10, 0)
    print(hash_table.insert(10, "bubble tea"))
    print(hash_table.insert(15, "coffee"))

    print(hash_table.getValue(10))

    print(hash_table.isOverLoadFactor())


def releaseMain() -> None:
    # You should update these three values as you test your implementation.
    hash_to_test = 0    
    initial_bucket_size = 10 
    initial_num_to_add = 100

    hash_table = HashTable(initial_bucket_size, hash_to_test)
    with open('hwk4-people.csv') as csv_file:    
        csv_reader = csv.reader(csv_file, delimiter=',')
        header = csv_reader.__next__() # pyright: ignore[reportUnusedVariable]
        for row_iterator in range(initial_num_to_add): # pyright: ignore[reportUnusedVariable]
            row = csv_reader.__next__()
            hash_table.insert(int(row[0]),row[1])
        print("Hash Map Initialized")
                
        option = ""
        while option != "QUIT":
            option = input("Select an option (ADD, GET, REMOVE, PRINT, CHECK, REHASH, QUIT): ").upper()        

            if option == "ADD":
                row = csv_reader.__next__()
                hash_table.insert(int(row[0]),row[1])
                print("Added - Key:", int(row[0]), "\tValue:", row[1])
            elif option == "GET":
                key = int(input("Which # would you like to get the value of? "))
                val = hash_table.getValue(key)
                if val is None:
                    print("Error,", key, "not found.")
                else:
                    print(val)
            elif option == "REMOVE":
                key = int(input("Which # would you like to remove? "))
                suc = hash_table.remove(key)
                if suc:
                    print(key, "was removed.")
                else:
                    print("Error,", key, "was not removed.")                    
            elif option == "PRINT":
                print(hash_table)   # calls the __str__ method.  
            elif option == "CHECK":
                isOver = hash_table.isOverLoadFactor()
                if isOver:
                    print("Your load factor is over 0.7, it's time to rehash.")
                else:
                    print("Load factor is ok.")
            elif option == "REHASH":
                suc = hash_table.reHash()
                if suc:
                    print("Rehash was successful.")
                else:
                    print("ERROR: rehash failed.")
            elif option == "QUIT" or option == "Q":
                break 
            else:
                print("Error: invalid input, please try again.")
                
        print("Goodbye!")
            

def profilerMain() -> None:    
    # You should update these three values as you profile your implementation.
    num_hash_implemented = 2    
    initial_bucket_size = 10 
    initial_num_to_add = 100

    for i in range(0, num_hash_implemented):        
        hash_table = HashTable(initial_bucket_size, i)
        with open('hwk4-people.csv') as csv_file:    
            csv_reader = csv.reader(csv_file, delimiter=',')
            header = csv_reader.__next__()  # pyright: ignore[reportUnusedVariable]
            for row_iterator in range(initial_num_to_add): # pyright: ignore[reportUnusedVariable]
                row = csv_reader.__next__()
                hash_table.insert(int(row[0]),row[1])
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
        
    

if __name__ == "__main__":
    # Swap these options to profile or test your code.
    testMain()
    #profilerMain()     
    #releaseMain()
    
