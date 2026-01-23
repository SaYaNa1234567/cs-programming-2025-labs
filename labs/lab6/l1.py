rates = {'h': 3600, 'm': 60, 's': 1}
while True:
    s = input()
    if not s: break
    
    val, dst = s.split()
    
    for i in range(len(val)):
        if not val[i].isdigit():
            num = float(val[:i])
            src = val[i:]
            break
    res = num * rates[src] / rates[dst]
    print(res, dst)
