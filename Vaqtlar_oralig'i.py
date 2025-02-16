with open("input.txt", "r") as file:
    h1, m1, s1 = map(int, file.readline().split())
    h2, m2, s2 = map(int, file.readline().split())

t1 = h1 * 3600 + m1 * 60 + s1
t2 = h2 * 3600 + m2 * 60 + s2

result = t2 - t1

with open("output.txt", "w") as file:
    file.write(str(result) + "\n")