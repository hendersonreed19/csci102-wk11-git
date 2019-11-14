# fibonacci.py

def fib():
    fibs = [1, 2]

    for i in range(0,8):
        num1 = fibs[i]
        a = i+1
        num2 = fibs[a]
        new = num1 + num2 
        fibs.append(new)
    return fibs

def main():
    print('OUTPUT', fib())

if __name__ == "__main__":
    main()
