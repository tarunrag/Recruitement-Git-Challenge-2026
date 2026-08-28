while True:
    print("SORTING AND CHECKING LIST\n")
    lst = list(input("Enter elements into list   : "))
    tn =  int(input("Enter element to be checked: "))
    print()

    for i in lst:
        j = lst.index(i)
        while j > 0:
            if lst[j-1] > lst[j]:
                lst[j-1], lst[j] = lst[j], lst[j-1]
            else:
                break

            j -= 1
    print(lst)
    print()
    for i in lst:
        if i == tn:
            print("True\n")
            break
        else:
            print("False\n")
            break
        
    if input("Do you want to continue (y/n): ") not in 'Yy':
        break


