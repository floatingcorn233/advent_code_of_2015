f=open("day_01 txt","r")
txt=f.read()
layer=0
devel=0
for i,kh in enumerate(txt):
    if kh=='(':
        layer+=1
    else:
        layer-=1

print(layer)

