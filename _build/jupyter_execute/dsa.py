#!/usr/bin/env python
# coding: utf-8

# # Data Structures

# 1. [Linked List](#linked-list)
# 2. [Binary Search Tree](#binary-search-tree)
# 3. [n-ary Tree](#n-ary-tree)
# 4. [Heap](#heaps)
# 5. [Trie](#trie)

# ## Linked List

# - Linked lists are a data structure that store a collection of elements. 
# - Each element is a node that contains a value and a pointer to the next node. 
# - The first node is called the head, and the last node is called the tail. 
# - The tail node points to `None`.

# In[1]:


class Node:
    def __init__(self, data):
        self.data = data 
        self.next = None

class LinkedList(Node):
    def __init__(self):
        self.head = None # head is the first node in the list

    def insert(self, data):
        if self.head is None: # if the list is empty
            self.head = Node(data)
        else: # if the list is not empty
            new_node = Node(data)
            new_node.next = self.head # Insert the new node at the beginning of the list
            self.head = new_node

    def print_list(self):
        temp = self.head 
        print("List: ", end="")
        while temp:
            print(temp.data)
            temp = temp.next

    def delete(self, data):
        if self.head is None:
            print("List is empty")
            return
        if self.head.data == data: # if the node to be deleted is the first node
            self.head = self.head.next
            return
        temp = self.head
        while temp.next is not None:
            if temp.next.data == data:
                break
            temp = temp.next
        if temp.next is None:
            print("Node not found")
        else:
            temp.next = temp.next.next


if __name__ == "__main__":
    llist = LinkedList()
    llist.insert(1)
    llist.insert(2)
    llist.insert(3)
    llist.insert(4)
    llist.print_list()
    llist.delete(3)
    llist.print_list()


# ## Binary Tree

# In[2]:


class Node:
    def __init__(self, data):
        self.data = data
        self.right = None
        self.left = None


class BinaryTree(Node):
    def __init__(self):
        self.root = None
    
    def populate(self, arr):
        '''
        arr: list of integers in inorder traversal, None represents null node. 
        '''

        def _populate(arr, start, end):
            if start > end:
                return None
            root = Node(arr[start])
            root.left = _populate(arr, start*2+1, end)
            root.right = _populate(arr, start*2+2, end)
            return root

        self.root = _populate(arr, 0, len(arr)-1)


    
    def print_tree(self):
        def _print_tree(root):
            if root is None:
                return
            print(root.data)
            _print_tree(root.left)
            _print_tree(root.right)

        _print_tree(self.root)

if __name__ == "__main__":
    arr = [1, 3, None, 5, None, 7, 9]
    tree = BinaryTree()
    tree.populate(arr)
    tree.print_tree()    


# ## Binary Search Tree
# 
# - A binary search tree is a tree data structure in which each node has at most two children, which are referred to as the left child and the right child.
# - The left subtree of a node contains only nodes with keys less than the node's value.
# - The right subtree of a node contains only nodes with keys greater than the node's value.
# - The left and right subtree each must also be a binary search tree.

# In[3]:


class Node:
    def __init__(self, data):
        self.data = data 
        self.right = None
        self.left = None
    
class BinarySearchTree(Node):
    def __init__(self):
        self.root = None
    
    def insert(self, data):
        ''' Insert a node in the BST '''
        if self.root is None:
            self.root = Node(data)
        else:
            self._insert(data, self.root)
    
    def _insert(self, data, curr_node): 
        ''' Recursive helper function to insert a node in the BST '''
        if data < curr_node.data:
            if curr_node.left is None:
                curr_node.left = Node(data)
            else:
                self._insert(data, curr_node.left)
        elif data > curr_node.data:
            if curr_node.right is None:
                curr_node.right = Node(data)
            else:
                self._insert(data, curr_node.right)
        else:
            print("Value already in tree")
    
    def print_tree(self, traversal_type="inorder"):
        '''
        Print the tree in the specified traversal type
        traversal_type: inorder, preorder, postorder
        '''
        if self.root is not None:
            self._print_tree(self.root, traversal_type)
    
    def _print_tree(self, curr_node, traversal_type):
        """
        Recursive helper function to print the tree in the specified traversal type
        """
        if curr_node is not None:
            if traversal_type == "inorder":
                self._print_tree(curr_node.left, traversal_type)
                print(curr_node.data)
                self._print_tree(curr_node.right, traversal_type)
            elif traversal_type == "preorder":
                print(curr_node.data)
                self._print_tree(curr_node.left, traversal_type)
                self._print_tree(curr_node.right, traversal_type)
            elif traversal_type == "postorder":
                self._print_tree(curr_node.left, traversal_type)
                self._print_tree(curr_node.right, traversal_type)
                print(curr_node.data)

if __name__ == "__main__":
    tree = BinarySearchTree()
    tree.insert(10)
    tree.insert(5)
    tree.insert(15)
    tree.insert(2)
    tree.insert(7)
    tree.insert(12)
    tree.insert(17)
    tree.print_tree("inorder")


# ## n-ary Tree
# - A special case of a tree, where each node $i$ has $n_i$ children.

# In[4]:


class Node:
    def __init__(self, data):
        self.data = data
        self.children = []
        
class SpecialBinaryTree(Node):
    def __init__(self):
        self.root = None
    
    def insert(self, data):
        if self.root is None:
            self.root = Node(data)
        else:
            new_node = Node(data)
            self.root.children.append(new_node)
                
        

    def print_tree(self, node):
        if node is None:
            return
        print(node.data)
        for child in node.children:
            self.print_tree(child)
            
if __name__ == "__main__":
    tree = SpecialBinaryTree()
    tree.insert(1)
    tree.insert(2)
    tree.insert(3)
    tree.insert(4)
    tree.insert(5)
    tree.insert(6)
    tree.print_tree(tree.root)


# More TODO:
# - [x] Implement a n-children tree
# - [ ] Implement a n-children tree with a parent pointer
# - [ ] Implement an insert method with a parent pointer
# - [ ] Implement a delete method 

# ## Heaps

# 
# 
# -  A heap is a complete binary tree, where each node is greater than all of its children.
# -  A heap is implemented using a list.
# -  The following operations are supported:
# -  push(x) -- Push element x onto heap.
# -  pop() -- Removes the element on top of the heap.
# -  top() -- Get the top element.
# -  empty() -- Return whether the heap is empty.
# 
# 
# **Note**: Minimum heap is the only heap that is implemented in Python.

# `heapify()` is a function that takes a list and turns it into a heap.

# In[5]:


import heapq

li = [10, 21, 11, 5,12]
heapq.heapify(li)

print("After heapify: ", li)


# In[6]:


li.append(1)
heapq.heapify(li)
print("After appending 1: ", li)


# `heappop()` is a function that pops the smallest element from the heap.

# In[7]:


heapq.heappop(li)
print("After popping: ", li)


# `heapq.heappush(heap, item)` pushes the value item onto the heap, maintaining the heap invariant.

# In[8]:


heapq.heappush(li, 2)
print("After pushing 2: ", li)


# `heapq.heappushpop(heap, item)` pushes the value item onto the heap, and then pops and returns the smallest element from the heap. The combined action runs more efficiently than `heappush()` followed by a separate call to `heappop()`.

# In[9]:


heapq.heappushpop(li, 3)
print("After pushingpop 3: ", li)


# ## Trie

# A trie is a nested tree data structure that stores strings. It is mostly used for searching strings with a common prefix.
# 
# Structure of a trie:
# - A `TrieNode` can have 26 children nodes of type `TrieNode`. 
# - Each node represents a letter in the alphabet.
# - `is_word` is a boolean that indicates whether the node is the end of a word.
# 
# 
# 
# 
# 

# In[10]:


class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end = False

class Trie:
    def __init__(self):
        self.root = TrieNode()
    
    def insert(self, word):
        curr_node = self.root
        for char in word:
            if char not in curr_node.children: 
                curr_node.children[char] = TrieNode() 
            curr_node = curr_node.children[char]
        curr_node.is_end = True
    
    def search(self, word):
        curr_node = self.root
        for char in word:
            if char not in curr_node.children:
                return False
            curr_node = curr_node.children[char]
        return curr_node.is_end
    
    def starts_with(self, prefix):
        curr_node = self.root
        for char in prefix:
            if char not in curr_node.children:
                return False
            curr_node = curr_node.children[char]
        return True
    
    def print_tree(self):
        def print_tree_helper(curr_node, word):
            if curr_node.is_end:
                print(word)
            for char in curr_node.children:
                print_tree_helper(curr_node.children[char], word + char)
        print_tree_helper(self.root, "")

if __name__ == "__main__":
    trie = Trie()
    trie.insert("apple")

    print(trie.search("apple"))
    print(trie.search("app"))
    
    print(trie.starts_with("app"))
    
    trie.insert("app")
    
    print(trie.search("app"))

    trie.insert("banana")
    
    trie.print_tree()


# In[ ]:




