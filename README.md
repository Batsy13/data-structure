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


<hr>

# Credits

All the content in here was acquired via course/channel of Augusto Galego:
<ul>
  <li> <a href="https://app.hub.la/m/L8wi9vio7WPnWbmF8ZIO"> Augusto Galego's Data Structures Course</a></li>
  <li> <a href="https://www.youtube.com/@GutoGalego">Augusto Galego's YouTube Channel</a></li>
</ul>

# Contact

Feel free to connect with me!

* **LinkedIn**: [@Pedro Costa](https://www.linkedin.com/in/pedro-costa-b189262b3/)

<p align="right">(<a href="#readme-top">back to top</a>)</p>

[Course-url]: https://www.google.com/url?sa=t&source=web&rct=j&opi=89978449&url=https://hub.la/g/L8wi9vio7WPnWbmF8ZIO&ved=2ahUKEwjZu8_ll7OOAxWurpUCHYntOvMQFnoECAkQAQ&usg=AOvVaw09lXlXgIJ-NWam1f2zBadn
[Galego-url]: https://www.youtube.com/@GutoGalego
