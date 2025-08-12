def firstRepeat(s):
    seen = set()
    for ch in s:
     if ch in seen:
           return ch
        seen.add(ch)
    return None

s = input()
result = firstRepeat(s)
if result:
        print(result)
else:
    print("No repeats")
