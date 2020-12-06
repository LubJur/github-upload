poc_kop = int(input())
prva_kopka = input().split()
druha_kopka = input().split()

for i in range(poc_kop):
    prva_kopka[i] = int(prva_kopka[i])

for i in range(poc_kop):
    druha_kopka[i] = int(druha_kopka[i])

def obsah_par(a):
    for i in range(len(a)):
        if a[i]%2 == 0:
            return True

def obsah_nepar(a):
    for i in range(len(a)):
        if a[i]%2 != 0:
            return True

if sum(prva_kopka)%2 == 0 and sum(druha_kopka)%2 == 0:
    if obsah_par(prva_kopka) and obsah_par(druha_kopka) == True:
        print("ano")
    elif obsah_nepar(prva_kopka) and obsah_nepar(druha_kopka) == True:
        print("ano")
    else:
        print("nie")

elif sum(prva_kopka)%2 != 0 and sum(druha_kopka)%2 != 0:
    if obsah_par(prva_kopka) and obsah_nepar(druha_kopka) == True:
        print("ano")
    elif obsah_nepar(prva_kopka) and obsah_par(druha_kopka) == True:
        print("ano")
    else:
        print("nie")

else:
    print("nie")
