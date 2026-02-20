f=open("day_01 txt","r")
txt=f.read()
layer=0
demon=0
for i,kh in enumerate(txt):
    if kh=='(':
        layer+=1
    else:
        layer-=1
    if layer==-1:
        demon=i+1
        break
print(demon)

