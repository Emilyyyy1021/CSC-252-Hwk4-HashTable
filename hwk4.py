# Name:  - Emily Wang & Tanya Chen
# Peers:  - names of CSC252 students who you consulted or ``N/A'' <br>
# References:  - URL of resources used <br>
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
        self.next = None
        
    def __str__(self) -> str:
        """ Returns a string representation of the object.
        :return : (str) a string description of the HashNode object.
        """
        return "{key:" + str(self.key) + ", value:" + self.value + "}"     
### END OF DO NOT EDIT###

# Hint: create a linked list class here...
class Node:
    """Class to instantiate linked list node objects
    >>> node = Node(Matt Damon)
    >>> print(node)
    Matt Damon
    """
     
    def __init__(self, data: str) -> None:
        self.data = data
        self.next: Node | None = None 

    def __str__(self) -> str:
        return "{data:" + str(self.data) + "}"   
    

class HashTable:
    
    def __init__(self, size:int, hash_choice:int) -> None:
        self.size = size
        self.hash_choice = hash_choice                  # Which hash function you will use.
        #TODO Finish constructor...
        self.array = [None] * size
    
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
            pass #TODO Implement your has functions here.
        elif self.hash_choice == 3:
            pass #TODO Implement your has functions here.
        elif self.hash_choice == 4:
            pass #TODO Implement your has functions here.
        return None
    
    def insert(self, key:int, val:str) -> bool:
        index = self.hashFunc(key) #find index with hash function
        if index is None: #no index
            return False
        slot = self.array[index] #yes index
        if slot == None: #put the value into the array 
            slot = val
            return True
        elif slot != None: #something in the slot
            if slot == str: 
                slot = Node(slot) #make first slot into linked list
                slot.next = Node(val) #attach new node
                return True
            else:
                while slot.next is not None: #attach the node to the end
                    slot = slot.next
                slot.next = Node(val)
                return True
        return False

    def getValue(self, key:int) -> str|None:
        
        return None

    def remove(self, key:int) -> bool:
        return False
    
    def isOverLoadFactor(self) -> bool:
        return False
    
    def reHash(self) -> bool:
        return False

def testMain() -> None:            
    # Use this function to test your code as you develop, especially your singly-linked list. 
    # Review, but do not use, profileMain or releaseMain until you are well into development.
    pass


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
    
