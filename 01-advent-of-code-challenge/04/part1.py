with open("input.txt", "r") as f:
    data = f.read()

out = 0

for l in data.split("\n"):
    a, b = l.split(",")
    x0, y0 = map(int, a.split('-'))
    x1, y1 = map(int, b.split('-'))

    if x0 >= x1 and y0 <= y1:
        out += 1
    elif x1 >= x0 and y1 <= y0:
        out += 1

print(out)