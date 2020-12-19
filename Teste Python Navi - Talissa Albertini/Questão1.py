lista = [] 
i = 1
while i <= 5000000:
    if i%2==0 and i%49==0 and i%37==0:
        lista.append(i)
    i+=1 
print(len(lista))




