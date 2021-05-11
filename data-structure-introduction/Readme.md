<h1 style="color:#6495ED">Introduction to Data Structure in Python</h1>
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
