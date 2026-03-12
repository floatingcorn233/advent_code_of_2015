with open("day_01 txt","r") as f:
    txt=f.read()
layer=0
devel=0
for kh in txt:
    if kh=='(':
        layer+=1
    else:
        layer-=1
print(layer)

