def canPowerup(n):
    if n <= 0:
        return False
    while n > 1:
        if n % 2 != 0:
            return False
        n //= 2
    return True

n = int(input())
print("Yes" if canPowerup(n) else "No")
