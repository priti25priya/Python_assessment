def Sets(sub, A, B):
    total = 0
    for i in sub:
        if i in A:
            total += 1
        elif i in B:
            total -= 1
        else:
            total += 0

    return total
