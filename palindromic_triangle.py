
n = int(input("Ingrese el numero "))

def main(n):
    buffer = ""
    if n == 1:
        print(n)
    else:
        for i in range(1,n+1):
            buffer += str(i)
        print(buffer)
        main(n-1)
main(n)