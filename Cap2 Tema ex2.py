#ex2 Cereți ca input de la utilizator 2 nume. Verificati si afisati:
#- Lungimea primului nume
#- Dacă cele doua nume date sunt la fel
#- Dacă primul nume este mai lung decat al doilea nume
#- Inițiala primului nume
#- Primul nume inversat

a=input("Spune-mi un nume :) : ")
b=input("Fain, mai spune-mi un nume :) : ")
print(len(a), a==b, len(a)>len(b), a[0], a[::-1])
