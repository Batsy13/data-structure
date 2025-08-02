<a id="readme-top"></a>

<br />
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#data-structure">Data Structure</a>
      <ul>
        <li>
          <a href="#big-o-notation">Big O Notation</a>
          <ul>
            <li><a href="#time-complexity">Time Complexity</a></li>
            <li><a href="#space-complexity">Space Complexity</a></li>
            <li><a href="#complexity">Complexity</a></li>
            <li><a href="#o1">O(1)</a></li>
            <li><a href="#olog-n">O(log n)</a></li>
            <li><a href="#on">O(n)</a></li>
            <li><a href="#on-log-n">O(n log n)</a></li>
            <li><a href="#on2">O(n²)</a></li>
            <li><a href="#sorts-complexity">Sorts Complexity</a></li>
          </ul>
        </li>
      </ul>
    </li>
    <li>
      <a href="array">Array</a>
      <ul>
        <li><a href="two-pointer">Two Pointer</a></li>
        <li><a href="sliding-window">Sliding Window</a></li>
        <li><a href="exponential-search">Exponential Search</a></li>
      </ul>
    </li>
    <li>
      <a href="linked-list">Linked List</a>
      <ul>
        <li><a href="creating-a-linked-list">Creating a Linked List</a></li>
        <li><a href="linked-list-functions">Linked List Functions</a></li>
      </ul>
    </li>
    <li>
      <a href="stack">Stack</a>
      <ul>
        <li><a href="implementing-a-stack">Implementing a Stack</a></li>
      </ul>
    </li>
    <li><a href="#credits">Credits</a></li>
    <li><a href="#contact">Contact</a></li>
  </ol>
</details>

<img width="1145" height="420" alt="image" src="https://github.com/user-attachments/assets/cd8e6dc8-f179-46c8-a68a-353264400ce4"/>


# Data Strucutre

This repository serves as a personal learning hub for the Data Structures course taught by Augusto Galego. Here, you'll find my solutions to exercises, code examples, and notes covering various data structures and algorithms.

## Big O Notation

### Time Complexity

This concept refers to how the runtime of an algorithm grows as the size of its input increases. 

<div align="center">
  <img width="703" height="491" alt="image" src="https://github.com/user-attachments/assets/4fbc9e48-3720-428d-9f0a-ddfb92b08875" />
</div>

### Space Complexity

This concept measures the amount of memory space or storage an algorithm requires to run to completion, as a function of the input size. It accounts for all the space used by the algorithm

<div align="center">
  <img width="705" height="384" alt="image" src="https://github.com/user-attachments/assets/20b8159a-cf3d-468c-ae3d-574432a38d05" />
</div>

### Complexity

<div align="center">
  <img width="702" height="486" alt="image" src="https://github.com/user-attachments/assets/d611d966-b194-48a4-b091-c9777e28296d" />
</div>

### O(1)

O(1) stands for Constant Complexity. This means that the time or space required by an algorithm remains constant, regardless of the size of the input data (n). It's the most efficient form of complexity.

<strong>Accessing the first element of an array:</strong>
This operation takes the same amount of time whether the array has 10 elements or 10 billion elements. The computer just needs to go to the memory address of the array's start and read the value at that location. This is a direct memory access, which is why it's O(1).

### O(log n)

O(logn) stands for Logarithmic Complexity. As you increase the Input exponentially, the execution time increases linearly.

<table align="center">
  <thead>
    <tr>
      <th>Input (n)</th>
      <th>$\log_2(n)$ (Approximate Value)</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>10</td>
      <td>3.321928</td>
    </tr>
    <tr>
      <td>20</td>
      <td>4.321928</td>
    </tr>
    <tr>
      <td>40</td>
      <td>5.321928</td>
    </tr>
  </tbody>
</table>

#### Binary Search

To find the number was needed 3 searchs

<div align="center">
  <img width="553" height="277" alt="image" src="https://github.com/user-attachments/assets/f71f4676-65d1-4624-9ea3-89b421aec904" />
</div>


If our algorithm scaled in O(n), when we doubled the array, we would need 6 searches to find the desired number.

<div align="center">
  <img width="706" height="185" alt="image" src="https://github.com/user-attachments/assets/de306be6-ace2-4332-98e8-459b3b8e573f" />
</div>

When doubling the input, the execution time increased by only one.

```
# Python implementation

def binary_search(nums, n):
    lo = 0
    hi = len(nums)
    steps = 0
    while lo < hi:
        steps += 1
    mid = int((lo + hi) / 2)

    if nums(mid) == n:
        print("step: ", steps) # Steps Taken 
        return mid
    elif nums(mid) < n:
        lo = mid + 1
    else:
        hi = mid
    return -1
```

### O(n)

O(n) stands for Linear Complexity. This means that the time or space required by an algorithm grows directly and proportionally with the size of the input data (n).

<div align="center">
  <img width="555" height="250" alt="image" src="https://github.com/user-attachments/assets/b008ffda-f151-48d8-9d02-4be328b3dc1c" />
</div>

Can we affirm that when searching for '3' in an array, our algorithm performed better than O(n)? No. When analyzing Big O, we (normally) analyze the worst case of an algorithm; we take the pessimistic side. That is to say, this algorithm will continue to be O(n).

### O(N log N)

- Sorting (quicksort, mergesort)
- Divide and Conquer

<div align="center">
  <img width="703" height="385" alt="image" src="https://github.com/user-attachments/assets/2334b77d-d72a-45d0-b8d4-38e50db7e3b5" />
</div>

Since there are logn levels, and each level incurs O(n) work for combining, the total time complexity is O(n×logn).

### O(n²)

O(n²) stands for Quadratic Complexity. When an algorithm has quadratic complexity, its runtime or space requirements grow proportionally to the square of the input size (n).
It's a Loop in a Loop.

### Sorts Complexity

<table align="center">
  <thead>
    <tr>
      <th>Sorting</th>
      <th>Best Case</th>
      <th>Average Case</th>
      <th>Worst Case</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Selection Sort</td>
      <td>O(n<sup>2</sup>)</td>
      <td>O(n<sup>2</sup>)</td>
      <td>O(n<sup>2</sup>)</td>
    </tr>
    <tr>
      <td>Insertion Sort</td>
      <td>O(n)</td> <td>O(n<sup>2</sup>)</td>
      <td>O(n<sup>2</sup>)</td>
    </tr>
    <tr>
      <td>Bubble Sort</td>
      <td>O(n)</td> <td>O(n<sup>2</sup>)</td>
      <td>O(n<sup>2</sup>)</td>
    </tr>
    <tr>
      <td>Merge Sort</td>
      <td>O(N log N)</td>
      <td>O(N log N)</td>
      <td>O(N log N)</td>
    </tr>
    <tr>
      <td>Quick Sort</td>
      <td>O(N log N)</td>
      <td>O(N log N)</td>
      <td>O(n<sup>2</sup>)</td>
    </tr>
    <tr>
      <td>Tree Sort</td>
      <td>O(N log N)</td>
      <td>O(N log N)</td>
      <td>O(n<sup>2</sup>)</td>
    </tr>
  </tbody>
</table>

# Array

Teoricamente os itens de um array são alocados em um espaço contínuo na memória, eles ficam próximos um dos outros para facilitar o acesso. Cada item possui um índice, com um valor atribuído.

<div align="center">
  <img width="704" height="359" alt="image" src="https://github.com/user-attachments/assets/2a0369d9-c1c0-45a6-9afb-21d53b4c4fd0" />
</div>

```
// JavaScript Example

let arr = [1,2,"a",3,4];

console.log(arr[1]); // Print 2

```

```
// We initialize an array
let my_array: [i32; 4] = [1,2,3,4];

// It's not possible to change the array's size at RunTime
// This would result in a process that would have to move the allocated memory to another location
```
<div align="center">
  <img width="624" height="435" alt="image" src="https://github.com/user-attachments/assets/50b5b6ef-a217-421a-af91-5685b362edb1" />
</div>

With that, Rust does not allow you to change this primitive type during runtime.

```
const a = new ArrayBuffer(8)

// > a 
// ArrayBuffer {
//   [Uint8Contents]: <00 00 00 00 00 00 00 00>,
//   byteLength: 8
// }

const a8 = new Uint8Array(a)

// > a8
// Uint8Array(8) [
//   0, 0, 0, 0
//   0, 0, 0, 0
// ]

const a32 = new Uint32Array(a)

// > a32
// Uint32Array(2) [ 0, 0 ]

a32[0] = 4294967295

// Uint32Array(2) [ 4294967295, 0 ]

a

// ArrayBuffer {
//   [Uint8Contents]: <ff ff ff ff 00 00 00 00>,
//   byteLength: 8
// }

a8

// Uint8Array(8) [
//   255, 255, 255, 255
//     0,   0,   0,   0
// ]
```

## Two Pointer

Two Pointer (or "Two Pointers") is an algorithm technique used with arrays, initializing two pointers, one at the beginning and one at the end, to avoid needing to allocate additional memory space.

### Reverse Words in a String

If we have a phrase like "Car Tar", we should individually reverse the words within the string, resulting in: "Rac Rat".

<div align="center">
  <img width="704" height="358" alt="image" src="https://github.com/user-attachments/assets/0f59a294-737b-4b6b-9fe4-06bdd3dcbf42" />


  The two pointers will start at the beginning of the word. Pointer R will traverse the array until it finds a blank space or the end of the word:

  <img width="705" height="310" alt="image" src="https://github.com/user-attachments/assets/7f9119c7-53e8-4ace-8ae4-bb505b76c13e" />


  Let's go back one element and swap the letter at L with the one at R:


  <img width="707" height="328" alt="image" src="https://github.com/user-attachments/assets/c34ba841-0879-487d-bb84-3f0b93bbc3c9" />


  With that, we will increment L by 1 and decrement R by 1, until the pointers meet each other:


  <img width="707" height="312" alt="image" src="https://github.com/user-attachments/assets/8ed47c87-f234-4912-86ce-55577152ee83" />

  Now, let's make R move until after the blank space, and bring L along with it:


  <img width="704" height="359" alt="image" src="https://github.com/user-attachments/assets/0144d552-b95a-49a6-bf82-7d492a53caef" />


  After this, simply repeat the process, and you will have the string with the words reversed:


  <img width="706" height="340" alt="image" src="https://github.com/user-attachments/assets/24bb5f16-a7e7-4231-b85c-e5e5d7707c5e" />

</div>

This application serves (or works) in languages that allow array mutation. In our case, in Python, it's not allowed to mutate arrays, so we will need to create an extra variable where we will update it by concatenating the reversed words.

```
class Solution:
    def reverseWords(self, s):
        result = ''
        l, r = 0, 0

        while r < len(s):
            if s[r] != ' ':
                r += 1
            else:
                result += s[l:r+1][::-1]
                r += 1
                l = r

        result += ' '
        result += s[l:r + 2][::-1]
        return result[1:]
```

## Sliding Window

Sliding Window serves to find subarrays.
Example: Find the largest subarray that can repeat a letter once.

In the sliding window technique, the outer while loop will expand the window while the inner one will compress it.
First, we'll take the first element and expand the array, storing the count of each repeated letter in the current expansion within a hashmap (dictionary in Python).
First, we find 'b' and assign the number of 'b's that exist in the subarray:

<div align="center">
  <img width="706" height="433" alt="image" src="https://github.com/user-attachments/assets/76ed0a3f-5078-4cfa-a682-2b5947205c87" />

  We expand the array and store c:

  <img width="705" height="405" alt="image" src="https://github.com/user-attachments/assets/754428a5-4900-4e48-8f1f-6cc1bbad9d74" />

  We expand the array and find another b:

  <img width="709" height="340" alt="image" src="https://github.com/user-attachments/assets/4f72bf81-af25-42b1-9836-3b2ce45f8342" />  

  Here we found 3 occurrences of 'b', meaning our max will only be the subarray 'bcb':

  <img width="705" height="354" alt="image" src="https://github.com/user-attachments/assets/067d7af8-fe9d-48eb-8c24-dbfde8c326d2" />

  Upon finding the most ideal subarray for our case, we have:

  <img width="703" height="359" alt="image" src="https://github.com/user-attachments/assets/3ec54fab-9c68-4821-ad70-cb9ffae7669a" />
</div>

```
class Solution:
    def maximumLengthSubstring(self, s: str) -> int:
        l, r = 0, 0
        _max = 1
        counter = {}

        counter[s[0]] = 1

        while r < len(s) - 1:
            r += 1
            if counter.get(s[r]):
                counter[s[r]] += 1
            else:
                counter[s[r]] = 1

            while counter[s[r]] == 3:
                counter[s[l]] -= 1
                l += 1
            _max = max(_max, r - l + 1)
        
        return _max
```

## Exponential Search

<table>
  <thead>
    <tr>
      <th>Time Complexity</th>
      <th>Space Complexity</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>O(log n)</td>
      <td>O(1)</td>
    </tr>
  </tbody>
</table>

Let's start at the beginning of the array, and with each search, we'll double the number of positions we jump:
<br>

Searching for the number 14:

<div align="center">

  <img width="705" height="289" alt="image" src="https://github.com/user-attachments/assets/dd66eab4-5270-40f2-a3f6-d586bc83bd3a" />

  Skiping one:

  <img width="706" height="132" alt="image" src="https://github.com/user-attachments/assets/80770294-f181-4e6d-a958-ec0e24cf3e24" />

  Skiping two and leting the left pointer in the previous index of R

  <img width="708" height="130" alt="image" src="https://github.com/user-attachments/assets/b86f177a-f3d3-448c-bd51-08942df97435" />

  <img width="708" height="124" alt="image" src="https://github.com/user-attachments/assets/a992be9a-0892-44ff-9052-0712eb2663ee" />

  <img width="707" height="136" alt="image" src="https://github.com/user-attachments/assets/8b1f882d-9304-47e9-a3f7-5b6428708e03" />

  Now that our right pointer is greater than the number we are looking for, we have a subarray where our desired number will be:

  <img width="703" height="130" alt="image" src="https://github.com/user-attachments/assets/e681b91f-aa73-4810-b6f4-82562e03497c" />

  Inside this array we're gonna do a binary search
</div>

```
def binary_search(nums, n, lo=8, hi=None):
    if hi is None:
        hi = len(nums) - 1
    while lo < hi:
        mid = int((10 + hi) / 2)
    if nums[mid] == n:
        return mid
    elif nums[mid] < n:
        lo = mid + 1
    else:
        hi = mid
    return -1


def exponential_search(arr, target):
    if arr[0] == target:
        return 0
    n = len(arr)
    i = 1
    while i < n and arr[i] < target:
        i *= 2
    if arr[i] == target:
        return 1
    return binary_search(arr, target, 1 // 2, min(i, n - 1))
```

# Linked List

A linked list is a data structure that represents a sequence of nodes. In a singly linked list, each node
points to the next node in the linked list. A doubly linked list gives each node pointers to both the next
node and the previous node.

<div align="center">
  <img width="1099" height="452" alt="image" src="https://github.com/user-attachments/assets/a8fda7fb-82b2-43e6-9d50-263d09f92aed" />
</div>

Unlike an array, a linked list does not provide constant time access to a particular "index" within the list.
This means that if you'd like to find the Kth element in the list, you will need to iterate through K elements.

The benefit of a linked list is that you can add and remove items from the beginning of the list in constant
time. For specific applications, this can be useful.

<table align="center">
  <thead>
    <tr>
      <th></th>
      <th>Read/Access</th>
      <th>Insertion</th>
      <th>Deletion</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Linked List</td>
      <td>O(n)</td>
      <td>O(n)</td>
      <td>O(n)</td>
    </tr>
    <tr>
      <td>Array</td>
      <td>O(1)</td>
      <td>O(n)</td>
      <td>O(1)</td>
    </tr>
  </tbody>
</table>

## Creating a Linked List

Python Implementation

```
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

dll = DoublyLinkedList()

```

### Linked List Functions

#### Add ( Front )

```
    def add_to_front(self, value):
        new_node = Node(value)
        new_node.next = self.head

        if self.head:
            self.head.prev = new_node
        else:
            self.tail = new_node
        self.head = new_node
```
This function creates a new node with the given value. It then sets the new node's next pointer to the current head of the list, effectively making it the new first node. If the list was not empty previously, the old head's prev pointer is updated to point to this new_node. If the list was initially empty, this new_node also becomes the tail. Finally, the list's head is updated to point to the new_node.

#### Add ( End )

```
    def add_to_end(self, value):
        new_node = Node(value)
        new_node.prev = self.tail

        if self.head:
            self.tail.next = new_node
        else:
            self.head = new_node
        self.tail = new_node
```
This function creates a new node with the provided value. It sets the new_node's prev pointer to the current tail of the list, positioning it to become the new last node. If the list was not empty, the old tail's next pointer is updated to point to the new_node. If the list was empty, this new_node also becomes the head. The list's tail is then updated to point to the new_node.

#### Remove ( Front )

```
    def remove_from_front(self):

        if not self.head:
            return None
        removed_value = self.head.value
        self.head = self.head.next
        if self.head:
            self.head.prev = None
        else:
            self.tail = None
        return removed_value
```
This function removes the node at the front (head) of the list. It first checks if the list is empty; if so, it returns None. Otherwise, it stores the value of the current head node. The list's head pointer is then moved to the next node in the sequence. If there is still a head after the removal, its prev pointer is set to None since it's now the first node. If the list becomes empty as a result of this removal, the tail is also set to None. The value of the removed node is returned.

#### Remove ( End )

```
    def remove_from_end(self):
        
        if not self.tail:
            return None
        removed_value = self.tail.value
        self.tail = self.tail.prev
        if self.tail:
            self.tail.next = None
        else:
            self.head = None
        return removed_value
```
This function removes the node at the end (tail) of the list. It first checks if the list is empty; if so, it returns None. Otherwise, it stores the value of the current tail node. The list's tail pointer is then moved to the previous node in the sequence. If there is still a tail after the removal, its next pointer is set to None since it's now the last node. If the list becomes empty as a result of this removal, the head is also set to None. The value of the removed node is returned.

# Stack

<div align="center">
  <img width="705" height="620" alt="image" src="https://github.com/user-attachments/assets/a0595f1d-19e1-460b-8baf-8abdb86c9ab9" />
</div>

<div align="center">
  <img width="708" height="281" alt="image" src="https://github.com/user-attachments/assets/75333434-73d5-415f-a740-9d6021bacf69" />
</div>


## Implementing a Stack

A stack uses LIFO (last-in first-out) ordering. That is, as in a stack of dinner plates, the most recent item
added to the stack is the first item to be removed.

It uses the following operations:
<ul>
  <li>pop( ) : Remove the top item from the stack.</li>
  <li>push( item ): Add an item to the top of the stack.</li>
  <li>peek( ): Return the top of the stack.</li>
  <li>is Empty( ): Return true if and only if the stack is empty.</li>
  <li>size( ): Return the size of the stack.</li>
</ul>

```
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class Stack:
    def __init__(self):
        self.top = None
        self._size = 0
        
    def push(self, item):
        new_node = Node(item)
        new_node.next = self.top
        self.top = new_node
        self._size += 1
        
    def pop(self):
        if self._size == 0:
            raise IndexError("Empty Stack")
        
        popped_node = self.top
        self.top = popped_node.next
        self._size -= 1
        
        return popped_node.value
    
    def peek(self):
        if self._size == 0:
            raise IndexError("Empty Stack")
        
        return self.top.value
    
    def isEmpty(self):
        return self._size == 0
    
    def size(self):
        return self._size
    
stack = Stack()

if stack.isEmpty():
    print("Yes")
else: 
    print("No")

stack.push(1)
stack.push(2)
stack.push(3)

print("Pop: ", stack.pop())
print("Peek: ", stack.peek())
print("Size: ", stack.size())
```

<hr>

# Credits

All the content in here was acquired via course/channel of Augusto Galego:
<ul>
  <li> <a href="https://www.amazon.com/Cracking-Coding-Interview-Programming-Questions/dp/0984782850">Cracking the Coding Interview</a></li>
  <li> <a href="https://app.hub.la/m/L8wi9vio7WPnWbmF8ZIO"> Augusto Galego's Data Structures Course</a></li>
  <li> <a href="https://www.youtube.com/@GutoGalego">Augusto Galego's YouTube Channel</a></li>
</ul>

# Contact

Feel free to connect with me!

* **LinkedIn**: [@Pedro Costa](https://www.linkedin.com/in/pedro-costa-b189262b3/)

<p align="right">(<a href="#readme-top">back to top</a>)</p>

[Course-url]: https://www.google.com/url?sa=t&source=web&rct=j&opi=89978449&url=https://hub.la/g/L8wi9vio7WPnWbmF8ZIO&ved=2ahUKEwjZu8_ll7OOAxWurpUCHYntOvMQFnoECAkQAQ&usg=AOvVaw09lXlXgIJ-NWam1f2zBadn
[Galego-url]: https://www.youtube.com/@GutoGalego
