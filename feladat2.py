while True:
    nap = input("milyen nap van ma? ")

    try:
        if nap =="Hétfő":
            print("hétköznap")
            print("1 nap")
            break
        if nap =="Kedd":
            print("hétköznap")
            print("2 nap")
            break
        if nap =="Szerda":
            print("hétköznap")
            print("3 nap")
            break
        if nap =="Csütörtök":
            print("hétköznap")
            print("4 nap")
            break
        if nap =="Péntek":
            print("hétköznap")
            print("5 nap")
            break
        if nap =="Szombat":
            print("hétvége")
            print("6 nap")
            break
        if nap =="Vasárnap":
            print("hétvége")
            print("7 nap")
            break
        else:
            print("Nem jó ",end="")
    except Exception:
        print("error")






