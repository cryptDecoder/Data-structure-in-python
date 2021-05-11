<h1 style="color:#6495ED">Introduction to Data Structure in Python</h1>
<img src="https://github.com/cryptDecoder/Data-structure-in-python/blob/master/data-structure-introduction/assets/Capture.PNG" alt="Banner">
<h2 style="color:#FF5733">What is an algorithm?</h2>
<p>An algorithm in a set of instructions in sequence used to solve the problems</p>

---

```
Example of Algorithm
    addition of two numbers given by user
    Algorithm:
        step 1: Start
        step 2: Get value of variable x and variable y from user
        step 3: add x and y and store into the z
                z = x+y
                return z
        step 4: display sum
        step 5: stop
```

---

<h3 style="color:#40E0D0">Solving algorithm using python program</h3>

```
# this is example for addition of two numbers
def add(x, y):
    return x + y


if __name__ == '__main__':
    x, y = map(int, input("user inputs :").split())
    print(add(x, y))

```

----
<h3>Asymptotic Analysis: Big-O Notation and More</h3>
<p>Asymptotic notations are the mathematical notations used to describe the running time of an algorithm when the input tends towards a particular value or a limiting value.

For example: In bubble sort, when the input array is already sorted, the time taken by the algorithm is linear i.e. the best case.</p>
<p>There are mainly three asymptotic notations:<br>
Big-O notation<br>
Omega notation<br>
Theta notation
</p>