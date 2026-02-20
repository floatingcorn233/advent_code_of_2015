f=open("day_02 txt","r")
route=f.read()
santa_route=route[::2]
robo_route=route[1::2]

def giftsender(route):
    x=0
    y=0
    locations = {(0, 0)}
    for direction in route:
        if direction == '<':
            x=x-1
        elif direction == '>':
            x=x+1
        elif direction == '^':
            y=y+1
        elif direction == 'v':
            y=y-1
        locations.add((x,y))
    return locations

deliver1=giftsender(santa_route)
deliver2=giftsender(robo_route)
alldeliver=deliver1|deliver2

print(len(alldeliver))