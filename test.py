def sum_f (n):
    sum = 0
    i = 0
    while i <= n:
        sum = sum + (1/(((4*i)+1)**2))
        i = i + 1  
    return sum    


def main():
    n = int(input("Enter the positive number: "))
    print(round(sum_f(n),3))
    

if __name__ == '__main__':
    main()
