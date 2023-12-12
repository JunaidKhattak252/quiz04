def truthtable():
    t_list=[]
    for i in range(8):
        p=int(input("Enter value of p: "))
        q=int(input("Enter value of q: "))
        r=int(input("Enter value of r: "))
        t_list.append((p,q,r))

    print("Truth Table:")
    print("P | Q | R")
    print("_________")
    for row in t_list:
        print(f"{row[0]} | {row[1]} | {row[2]}")

    //question 01
    print("***Truth Table***")
    print("P | Q | R | (P --> Q) OR (Q --> R) | (P --> Q) AND (Q <--> R)")
    print("_______________________________________________________________")
    for row in t_list:
        a_result = (not row[0] or row[1]) or (not row[1] or row[2])
        b_result = (not row[0] or row[1]) and ((not row[1] or row[2]) and (not row[2] or row[1]))
        print(f"{row[0]} | {row[1]} | {row[2]} | {int(a_result)} | {int(b_result)}")


truthtable()


       



