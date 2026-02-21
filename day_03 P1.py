import pandas as pd

firehazard = pd.DataFrame(0, index=range(1000), columns=range(1000))

f = open("day_03 txt", "r")
instruction = f.read()

juzheng = instruction.split("\n")

def magic(line):
    a = line.split(" ")
    start = a[-3]
    end = a[-1]
    startpoint = start.split(",")
    endpoint = end.split(",")
    x1 = int(startpoint[0])
    y1 = int(startpoint[1])
    x2 = int(endpoint[0])
    y2 = int(endpoint[1])
    return x1, y1, x2, y2

for line in juzheng:

    x1, y1, x2, y2 = magic(line)

    if "turn on" in line:
        firehazard.loc[x1:x2, y1:y2] = 1
    elif "turn off" in line:
        firehazard.loc[x1:x2, y1:y2] = 0
    elif "toggle" in line:
        firehazard.loc[x1:x2, y1:y2] = 1 - firehazard.loc[x1:x2, y1:y2]

print(int(firehazard.to_numpy().sum()))