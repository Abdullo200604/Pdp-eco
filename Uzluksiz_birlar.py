def son(s):
    if "10" in s.strip("0") and "01" in s.strip("0"):
        print("NO")
    else:
        print("YES")


s = input().strip()
son(s)