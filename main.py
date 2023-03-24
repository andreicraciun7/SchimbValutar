while True:
    print("""
       1. RON
       2. EUR
       3. GBP
       """)
    moneda_initiala = str(input("Moneda pe care doriți să o schimbați:"))

    if moneda_initiala == "1":
        suma_initiala = float(input("Introduceți suma pe care doriți să o convertiți:"))
        moneda_schimb = input("Moneda în care doriți să convertiți suma introdusă:")

        if moneda_schimb == "1":
                print ("\nAlegeți o monedă diferită de cea curentă.")

        elif moneda_schimb == "2":
                print(round(suma_initiala / 5 , 2))

        elif moneda_schimb == "3":
                print(round(suma_initiala / 5.56 , 2))


    elif moneda_initiala == "2":
        suma_initiala = float(input("Introduceți suma pe care doriți să o convertiți:"))
        moneda_schimb = input("Moneda în care doriți să convertiți suma introdusă:")
        if moneda_schimb == "2":
                print ("\nAlegeți o monedă diferită de cea curentă.")

        elif moneda_schimb == "1":
                print(round(suma_initiala * 5 , 2))

        elif moneda_schimb == "3":
                print(round((suma_initiala * 5) / 5.56 , 2))


    elif moneda_initiala == "3":
        suma_initiala = float(input("Introduceți suma pe care doriți să o convertiți:"))
        moneda_schimb = input("Moneda în care doriți să convertiți suma introdusă:")
        if moneda_schimb == "3":
                print ("\nAlegeți o monedă diferită de cea curentă.")

        elif moneda_schimb == "1":
                print(round(suma_initiala * 5.56 , 2))

        elif moneda_schimb == "2":
                print(round((suma_initiala * 5.56) / 5 , 2))

    else:
        print("\n Valoarea introdusă este invalidă.")