from itertools import islice

def vytvor_list(org_list):
    for i in range(len(org_list)):
        org_list[i] = int(org_list[i])
    return org_list

def najdi_index_n_vyskytom(org_list, hladam, n):
    matches = (idx for idx, val in enumerate(org_list) if val == hladam)
    return next(islice(matches, n-1, n), None)

"""
    string = ""
    string.join(org_list)
    print("string po join:", string)
    inilist = [m.start() for m in re.finditer(hladam, string)]
    print("occurence", inilist[n])
    
    index_je = 0
    i = 0
    while i != n:
        index_je = org_list.index(hladam)
        print("index je:", index_je)
        org_list.pop(index_je)
        print("org_list_po_del:", org_list)
        i = i + 1
    print("i:",i)
    return index_je + (i - 1)
  
    for i in range(len(org_list)):
        if org_list[i] == hladam:
            najdene_poc = najdene_poc + 1
            print("najdene_poc:", najdene_poc)
            if najdene_poc == n:
                print("index hladaneho je:", i)
                return i
"""            

pzas_a_potaz = input().split()
pzas_a_potaz = vytvor_list(pzas_a_potaz)

zastavky = input().split()
zastavky = vytvor_list(zastavky)

otazky = []

for i in range(pzas_a_potaz[1]):
    otazka = input().split()
    otazka = vytvor_list(otazka)
    print(otazka)
    otazky.append(otazka)
    print(otazky)
#rozdelili sme si otazky do nested listu

for i in range(pzas_a_potaz[1]):
    print("------------------------------")
    rozsah = zastavky[otazky[i][0]-1:otazky[i][1]]
    print("rozsah:", zastavky[otazky[i][0]-1:otazky[i][1]])
    if otazky[i][2] in rozsah:
        if rozsah.count(otazky[i][2]) >= otazky[i][3]:
            ind_z_rozsahu = najdi_index_n_vyskytom(rozsah, otazky[i][2], otazky[i][3])
            print("index zastavky z rozsahu je:", ind_z_rozsahu)
            print("index zastavky zo zastavok je:", len(zastavky[:otazky[i][0]]) + ind_z_rozsahu)
        else:
            print(-1)
    else:
        print("nie je v rozsahu (-1)")
