for a in range(1, 5):
    for b in range(1, 5):
        for c in range(1, 5):
            if a != b and b != c and a != c:
                print(a, b, c)
        pass
    pass
