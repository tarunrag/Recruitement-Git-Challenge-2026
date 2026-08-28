while True:
    print("FREQUENCY AND REVERSING OF STRING\n")
    st = str(input("Enter string: "))
    fq = {}
    for ch in st:
        if ch in fq:
            fq[ch] += 1
        else:
            fq[ch] = 1

    for ch, c in fq.items():
        print(ch, ':', c)

    print("Reversed String: ", st[::-1])

    if input("Do you want to continue (y/n): ") not in 'Yy':
        break
        
        
        
