#1. Write a Python program to create a class representing a Circle. Include methods to calculate its area and perimeter.

import math 

class Circle:
    def __init__(self,radius):
        self.radius=radius

    def calculate_circle_area(self):
        return math.pi*self.radius**2

    def calculate_circle_perimeter(self):
        return 2*math.pi*self.radius

radius=float(input('Input the radius of circle:'))

circle=Circle(radius)

area=circle.calculate_circle_area()
perimeter=circle.calculate_circle_perimeter()

print('Area of the circle:', area)
print('Perimeter of the circle:', perimeter)
#2. Write a Python program to create a Person class. Include attributes like name, country, and date of birth. Implement a method to determine the person's age.

from datetime import date

class Person:
    def __init__(self, name, country, date_of_birth):
        self.name=name
        self.country=country
        self.date_of_birth=date_of_birth

    def calculate_age(self):
        today=date.today()
        age=today.year-self.date_of_birth.year
        if today< date(today.year, self.date_of_birth.month, self.date_of_birth.day):
           age -=1
        return age
    
person1=Person('Ferdi Odilia', 'France', date(1962,7,12))

print('Person 1:')
print('Name:', person1.name)
print('Country:', person1.country)
print('Date of Birth:', person1.date_of_birth)
print('Age:', person1.calculate_age())
#3. Write a Python program to create a Calculator class. Include methods for basic arithmetic operations.

class Calculator:
    def add(self,x,y):
        return x+y
    def substract(self,x,y):
        return x-y
    def multiply(self,x,y):
        return x*y
    def divide(self,x,y):
        if y!=0:
            return x/y
        else:
            return ('Cannot divide by zero')
        
Calculator=Calculator()

result=Calculator.add(7,5)
print('7+5=', result)

result=Calculator.substract(34,21)
print('34-21=', result)

result=Calculator.multiply(54,2)
print('54*2=', result)

result=Calculator.divide(144,2)
print('144/2=', result)

result=Calculator.divide(45,0)
print('45/0=', result)





        
#4. Shape Class with Subclasses for Different Shapes

import math 

class Shape:
    def calculate_are(self):
        pass
    def calculate_perimter(self):
        pass
class Circle (Shape):
    def __init__(self, radius):
        self.radius=radius
    def calculate_area(self):
        return math.pi*self.radius**2
    def calculate_perimter(self):
        return 2* math.pi*self.radius
    
class Rectangle (Shape):
    def __init__(self, length, width):
        self.length=length
        self.width=width
r=7
circle=Circle(r)
circle_area=circle.calculate_circle_area()
circle_perimeter=circle.calculate_circle_perimeter()

print('Radius of the circle:', r)
print('Circle Area:', circle_area)
print('Circle Perimeter', circle_perimeter)
        
        
        

#5. 

# Define a class called Node to represent a node in a binary search tree (BST)
class Node:
    # Initialize the Node object with a value, and set the left and right child pointers to None
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Define a custom __str__ method to convert the node's value to a string
    def __str__(self):
        return str(self.value)

# Define a class called BinarySearchTree to represent a binary search tree
class BinarySearchTree:
    # Initialize the BST with an empty root node
    def __init__(self):
        self.root = None

    # Insert a value into the BST
    def insert(self, value):
        # If the root is None, create a new node with the given value as the root
        if self.root is None:
            self.root = Node(value)
        else:
            self._insert_recursive(self.root, value)

    # Helper method to recursively insert a value into the BST
    def _insert_recursive(self, node, value):
        if value < node.value:
            if node.left is None:
                node.left = Node(value)
            else:
                self._insert_recursive(node.left, value)
        elif value > node.value:
            if node.right is None:
                node.right = Node(value)
            else:
                self._insert_recursive(node.right, value)

    # Search for a value in the BST
    def search(self, value):
        return self._search_recursive(self.root, value)

    # Helper method to recursively search for a value in the BST and return the node if found
    def _search_recursive(self, node, value):
        if node is None or node.value == value:
            return node
        if value < node.value:
            return self._search_recursive(node.left, value)
        else:
            return self._search_recursive(node.right, value)

# Example usage
# Create an instance of BinarySearchTree
bst = BinarySearchTree()

# Insert values into the BST
bst.insert(5)
bst.insert(3)
bst.insert(7)
bst.insert(2)
bst.insert(4)
bst.insert(6)
bst.insert(8)

# Search for elements in the BST and print the results
print("Searching for elements:")
print(bst.search(4))  # Found, returns the node (4)
print(bst.search(9))  # Not found, returns None 

#6. Write a Python program to create a class representing a stack data structure. Include methods for pushing and popping elements.


# Define a class called Stack to implement a stack data structure
class Stack:
    # Initialize the stack with an empty list to store items
    def __init__(self):
        self.items = []

    # Push an item onto the stack
    def push(self, item):
        self.items.append(item)

    # Pop (remove and return) an item from the stack if the stack is not empty
    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        else:
            return "Cannot pop from an empty stack."

    # Check if the stack is empty
    def is_empty(self):
        return len(self.items) == 0

    # Get the number of items in the stack
    def size(self):
        return len(self.items)

    # Peek at the top item of the stack without removing it, if the stack is not empty
    def peek(self):
        if not self.is_empty():
            return self.items[-1]
        else:
            return "Empty stack."

# Example usage
# Create an instance of the Stack class
stack = Stack()

# Push items onto the stack
stack.push(0)
stack.push(1)
stack.push(2)
stack.push(3)
stack.push(4)

# Print the size of the stack and the top element
print("Stack size:", stack.size())
print("Top element:", stack.peek())

# Pop an item from the stack, and print the popped item, and the updated size and top element
popped_item = stack.pop()
print("\nPopped item:", popped_item)
print("\nStack size:", stack.size())
print("Top element:", stack.peek())

#----------------------------------------
# Create another instance of the Stack class
stack1 = Stack()

# Print the size of the empty stack and attempt to pop an item (with an error message)
print("\nStack size:", stack1.size())
popped_item = stack1.pop()
print("\nPopped item:", popped_item) 

#7. Write a Python program to create a class representing a linked list data structure. Include methods for displaying linked list data, inserting, and deleting nodes.


# Define a class called Node to represent a node in a linked list
class Node:
    # Initialize the Node object with data and set the next pointer to None
    def __init__(self, data):
        self.data = data
        self.next = None

# Define a class called LinkedList to represent a singly linked list
class LinkedList:
    # Initialize the linked list with an empty head node
    def __init__(self):
        self.head = None

    # Display the elements in the linked list
    def display(self):
        current = self.head
        while current:
            print(current.data, end=" ")
            current = current.next
        print()

    # Insert a new node with the given data at the end of the linked list
    def insert(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node

    # Delete a node with the given data from the linked list
    def delete(self, data):
        if not self.head:
            return

        if self.head.data == data:
            self.head = self.head.next
            return

        current = self.head
        prev = None
        while current and current.data != data:
            prev = current
            current = current.next

        if current:
            prev.next = current.next

# Example usage
# Create an instance of the LinkedList class
linked_list = LinkedList()

# Insert elements into the linked list
linked_list.insert(1)
linked_list.insert(2)
linked_list.insert(3)
linked_list.insert(4)

# Display the initial linked list
print("Initial Linked List:")
linked_list.display()

# Insert a new node with data 5 into the linked list
linked_list.insert(5)
print("After inserting a new node (5):")
linked_list.display()

# Delete a node with data 2 from the linked list
linked_list.delete(2)
print("After deleting an existing node (2):")
linked_list.display() 

#8. Write a Python program to create a class representing a shopping cart. Include methods for adding and removing items, and calculating the total price.

# Define a class called ShoppingCart to represent a shopping cart
class ShoppingCart:
    # Initialize the shopping cart with an empty list of items
    def __init__(self):
        self.items = []

    # Add an item with a name and quantity to the shopping cart
    def add_item(self, item_name, qty):
        item = (item_name, qty)
        self.items.append(item)

    # Remove an item with a specific name from the shopping cart
    def remove_item(self, item_name):
        for item in self.items:
            if item[0] == item_name:
                self.items.remove(item)
                break

    # Calculate and return the total quantity of items in the shopping cart
    def calculate_total(self):
        total = 0
        for item in self.items:
            total += item[1]
        return total

# Example usage
# Create an instance of the ShoppingCart class
cart = ShoppingCart()

# Add items to the shopping cart
cart.add_item("Papaya", 100)
cart.add_item("Guava", 200)
cart.add_item("Orange", 150)

# Display the current items in the cart and calculate the total quantity
print("Current Items in Cart:")
for item in cart.items:
    print(item[0], "-", item[1])

total_qty = cart.calculate_total()
print("Total Quantity:", total_qty)

# Remove an item from the cart, display the updated items, and recalculate the total quantity
cart.remove_item("Orange")
print("\nUpdated Items in Cart after removing Orange:")
for item in cart.items:
    print(item[0], "-", item[1])

total_qty = cart.calculate_total()
print("Total Quantity:", total_qty) 

#9. Write a Python program to create a class representing a stack data structure. Include methods for pushing, popping, and displaying elements.

# Define a class called Stack to implement a stack data structure
class Stack:
    # Initialize the stack with an empty list to store items
    def __init__(self):
        self.items = []

    # Push an item onto the stack
    def push(self, item):
        self.items.append(item)

    # Pop (remove and return) an item from the stack if the stack is not empty
    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        else:
            raise IndexError("Cannot pop from an empty stack.")

    # Check if the stack is empty
    def is_empty(self):
        return len(self.items) == 0

    # Display the items in the stack
    def display(self):
        print("Stack items:", self.items)

# Example usage
# Create an instance of the Stack class
stack = Stack()

# Push items onto the stack
stack.push(10)
stack.push(20)
stack.push(30)
stack.push(40)
stack.push(50)

# Display the items in the stack
stack.display()

# Pop items from the stack and print the popped items
popped_item = stack.pop()
print("Popped item:", popped_item)
popped_item = stack.pop()
print("Popped item:", popped_item)

# Display the updated items in the stack
stack.display()

#10. Queue Data Structure Class

# Define a class called Queue to implement a queue data structure
class Queue:
    # Initialize the queue with an empty list to store items
    def __init__(self):
        self.items = []

    # Add (enqueue) an item to the end of the queue
    def enqueue(self, item):
        self.items.append(item)

    # Remove and return (dequeue) an item from the front of the queue if the queue is not empty
    def dequeue(self):
        if not self.is_empty():
            return self.items.pop(0)
        else:
            raise IndexError("Cannot dequeue from an empty queue.")

    # Check if the queue is empty
    def is_empty(self):
        return len(self.items) == 0

# Example usage
# Create an instance of the Queue class
queue = Queue()

# Enqueue (add) items to the queue
queue.enqueue(10)
queue.enqueue(20)
queue.enqueue(30)
queue.enqueue(40)
queue.enqueue(50)

# Print the current items in the queue
print("Current Queue:", queue.items)

# Dequeue (remove) items from the front of the queue and print the dequeued items
dequeued_item = queue.dequeue()
print("Dequeued item:", dequeued_item)
dequeued_item = queue.dequeue()
print("Dequeued item:", dequeued_item)

# Print the updated items in the queue
print("Updated Queue:", queue.items) 

#11. Bank Class for Managing Customer Accounts and Transactions

# Define a class called Bank to implement a simple banking system
class Bank:
    # Initialize the bank with an empty dictionary to store customer accounts and balances
    def __init__(self):
        self.customers = {}

    # Create a new account with a given account number and an optional initial balance (default to 0)
    def create_account(self, account_number, initial_balance=0):
        if account_number in self.customers:
            print("Account number already exists.")
        else:
            self.customers[account_number] = initial_balance
            print("Account created successfully.")

    # Make a deposit to the account with the given account number
    def make_deposit(self, account_number, amount):
        if account_number in self.customers:
            self.customers[account_number] += amount
            print("Deposit successful.")
        else:
            print("Account number does not exist.")

    # Make a withdrawal from the account with the given account number
    def make_withdrawal(self, account_number, amount):
        if account_number in self.customers:
            if self.customers[account_number] >= amount:
                self.customers[account_number] -= amount
                print("Withdrawal successful.")
            else:
                print("Insufficient funds.")
        else:
            print("Account number does not exist.")

    # Check and print the balance of the account with the given account number
    def check_balance(self, account_number):
        if account_number in self.customers:
            balance = self.customers[account_number]
            print(f"Account balance: {balance}")
        else:
            print("Account number does not exist.")

# Example usage
# Create an instance of the Bank class
bank = Bank()

# Create customer accounts and perform account operations
acno1= "SB-123"
damt1 = 1000
print("New a/c No.: ",acno1,"Deposit Amount:",damt1)
bank.create_account(acno1, damt1)

acno2= "SB-124"
damt2 = 1500
print("New a/c No.: ",acno2,"Deposit Amount:",damt2)
bank.create_account(acno2, damt2)

wamt1 = 600
print("\nDeposit Rs.",wamt1,"to A/c No.",acno1)
bank.make_deposit(acno1, wamt1)

wamt2 = 350
print("Withdraw Rs.",wamt2,"From A/c No.",acno2)
bank.make_withdrawal(acno2, wamt2)

print("A/c. No.",acno1)
bank.check_balance(acno1)

print("A/c. No.",acno2)
bank.check_balance(acno2)

wamt3 = 1200
print("Withdraw Rs.",wamt3,"From A/c No.",acno2)
bank.make_withdrawal(acno2, wamt3)

acno3 = "SB-134"
print("A/c. No.",acno3)
bank.check_balance(acno3)  # Non-existent account number 






















