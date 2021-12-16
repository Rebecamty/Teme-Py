# ex 3 . Folosind codul de la exercitiul 2, mai cereți input de la utilizator cu un număr:
# - Afisati primul nume multiplicat de n ori, unde n este numărul introdus de către
# utilizator.


a=input("Spune-mi un nume :) : ")
b=input("Fain, mai spune-mi un nume :) : ")
c=int(input("bun, ne mai trebuie un numar: "))
print(f"Lungimea primului nume este de: { len(a)} litere \n Sunt numele egale? {a==b} \n Primul nume este mai lung ca celalalt? {len(a)>len(b)} \n Prima litera din primul nume este: {a[0]} \n Primul nume intors este: {a[::-1]} \n Primul nume inmultit cu numarul pe care l-ai scris:) {a*c}")

