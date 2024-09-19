def calculate_years(N, X, M):
    years = 0
    while N < M:
        N += N * (X / 100)
        years += 1
    return years

def solve():
    t = int(input())
    for _ in range(t):
        N, X, M = map(float, input().split())
        years = calculate_years(N, X, M)
        print(years)

if __name__ == "__main__":
    solve()
