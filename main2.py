def truthtable():
    t_list = []
    
    for _ in range(8):  
        p = int(input("Enter value of p (0 or 1): "))
        q = int(input("Enter value of q (0 or 1): "))
        r = int(input("Enter value of r (0 or 1): "))
        t_list.append((p, q, r))

    print("Truth Table:")
    print("P | Q | R | (P --> Q) OR (Q --> R) | (P --> Q) AND (Q <--> R)")
    print("-" * 60)
    
    for row in t_list:
        formula_a_result = (not row[0] or row[1]) or (not row[1] or row[2])
        formula_b_result = (not row[0] or row[1]) and ((not row[1] or row[2]) and (not row[2] or row[1]))

        print(f"{row[0]} | {row[1]} | {row[2]} | {int(formula_a_result)} | {int(formula_b_result)}")

# Example usage:
truthtable()
