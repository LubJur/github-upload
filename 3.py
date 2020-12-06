from itertools import islice

pzas_a_potaz = input()
pzas_a_potaz = [int(i) for i in pzas_a_potaz.split()]

zastavky = input()
zastavky = [int(i) for i in zastavky.split()]

otazky = []

def najdi_index_n_vyskytom(org_list, hladam, n):
    matches = (idx for idx, val in enumerate(org_list) if val == hladam)
    foo = next(islice(matches, n-1, n), None)
    if foo == None:
        return -1
    else:
        return foo

for i in range(pzas_a_potaz[1]):
    otazka = input()
    otazka = [int(i) for i in otazka.split()]
    otazky.append(otazka)

for i in range(pzas_a_potaz[1]):
    rozsah = zastavky[otazky[i][0]-1:otazky[i][1]]
    if otazky[i][2] in rozsah:
        ind_z_rozsahu = najdi_index_n_vyskytom(rozsah, otazky[i][2], otazky[i][3])        
        if ind_z_rozsahu == -1:
            print(-1)
        else:
            print(len(zastavky[:otazky[i][0]]) + ind_z_rozsahu)
    else:
        print(-1)
