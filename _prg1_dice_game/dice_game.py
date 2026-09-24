import random
totalsumma = 0
fortsätta = True
while fortsätta:

    svar = input("vill du fortsätta spelet? ")
    if svar == "nej":
        print("wooow, du är för räddd, feeeegissss")
        fortsätta = False
    elif svar == "ja":
        print("okej, slår igen.")
        nummer = random.randint(1, 6)
        totalsumma = totalsumma + nummer
        print("du fick nummret", nummer)
    if totalsumma > 21:
        input("känner du dig klar du? ")
        print("du förlorade >:(")
        fortsätta = False
    elif totalsumma == 21:
      input("känner du dig klar nu? ")
      if svar == "ja":
             print("DU VANN!!!")
             fortsätta = False