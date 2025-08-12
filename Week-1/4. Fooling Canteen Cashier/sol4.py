def can_fool(N, X, prices):
    odd = sum(1 for p in prices if p % 2 == 1)
    even = N - odd
    for i in range(1, X + 1, 2):
        if i <= odd and X - i <= even:
            return True
    return False

N, X = map(int, input().split())
prices = list(map(int, input().split()))

print("hellye" if can_fool(N, X, prices) else "NO")
