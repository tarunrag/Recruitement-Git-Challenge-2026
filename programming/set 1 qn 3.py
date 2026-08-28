while True:
    print("SHIFTING ALPHABETS\n")

    st  = str(input("Enter string: "))
    st2 = ''
    for i in st:
        if i.isupper():
            nc = chr((ord(i) - 65 + 2) % 26 + 65)
            st2 += nc
        elif i.islower():
            nc = chr((ord(i) - 97 + 2) % 26 + 97)
            st2 += nc
        else:
            st2 += i
    print("Result: ", st2)
    
    if input("Do you want to continue(y/n): ") not in 'Yy':
        break

    
