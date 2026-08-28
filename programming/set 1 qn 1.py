while True:
    print("INPUTTING AND DECODING\n")

    print("Menu\n")
    print("'x'  = 0\n")
    print("'ox' = 1\n")
    print("'oo' = 2\n")
    ch = input("Enter string: ")
    print()
    o = ch.replace('oo', '2').replace('ox', '1').replace('x', '0')
    print("OUTPUT: ", o)

    if input("Do you want to continue (y/n): ") not in 'Yy':
        break
        
        
