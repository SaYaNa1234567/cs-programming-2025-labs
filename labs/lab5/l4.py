def sort_tuple(t):
    try:
        return tuple(sorted(t))
    except TypeError:
        return t

tuple1 = (5, 2, 8, 1, 9)
tuple2 = (5, 2, "hello", 1)

print(sort_tuple(tuple1))  
print(sort_tuple(tuple2))  
