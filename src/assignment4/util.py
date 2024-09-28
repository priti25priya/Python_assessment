def merge(s, k):
    for i in range(0, len(s), k):
        substring = s[i:i + k]
        seen = set()
        u = ''
        for char in substring:
            if char not in seen:
                u += char
                seen.add(char)
        print(u)
