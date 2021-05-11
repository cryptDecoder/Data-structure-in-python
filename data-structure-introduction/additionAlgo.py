# this is example for addition of two numbers
def add(x, y):
    return x + y


if __name__ == '__main__':
    x, y = map(int, input("user inputs :").split())
    print(add(x, y))
