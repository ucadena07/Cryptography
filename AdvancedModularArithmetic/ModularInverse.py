def modular_inverser(a, m):
    for inv in range(0,m):
        if(a * inv) % m == 1:
            return inv
    
    print("There is no modular inverse")