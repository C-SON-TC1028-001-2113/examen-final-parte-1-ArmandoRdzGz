def main():
    num = int(input("Enter a number: "))
    largo = len(str(num))
    #escribe tu código abajo de esta línea
    
    if largo<=6:
        if num>0:
            a = int(str(num)[::-1])
            print (a)
        elif num<0:
            b = num*-1
            c = int(str(b)[::-1])
            d = c*-1
            print (d)
    else:
        print("Too long")


if __name__=='__main__':
    main()
