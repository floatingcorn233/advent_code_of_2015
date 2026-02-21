with open("day_02 txt","r") as f:
    route=f.read()
x=0
y=0
locations = {(0,0)}
location=(0,0)

for direction in route:
    if direction == '<':
        x=x-1
    elif direction == '>':
        x=x+1
    elif direction == '^':
        y=y+1
    elif direction == 'v':
        y=y-1
    location={(x,y)}
    locations.add((x,y))
print(len(locations))
