def is_lucky_number(n):
    for digit in n:
        if digit != '4' and digit != '7':
            return False
    return True

def solve():
    t = int(input())
    for _ in range(t):
        n = input().strip()
        if is_lucky_number(n):
            print("YES")
        else:
            print("NO")

if __name__ == "__main__":
    solve()
