#ex4  Declarați o variabila cu șirul: “Ananas”. Afișati șirul în următoarele feluri pe ecran: -A
#n a n a s
#- Ana nas
#- An:ana:s
#- Ana_na_s
#- nananananananana

a="Ananas"
'''
for i in a:
    print(i)

'''

print(a[0],a[1],a[2],a[3],a[4],a[5], sep="\n")

b=a[:len(a)//2]
c=a[len(a)//2:]
print(b,c, sep="\n")

d=a[:2]
e=a[2:5]
f=a[5:6]
g=a[:3]
h=a[3:5]
print(d,e,f, sep=":")
print(g,h,f, sep="_")
print(h*8)
