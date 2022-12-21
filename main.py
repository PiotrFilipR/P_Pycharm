
# przywitanie

print("Witaj w programie, który wyliczy wysokość Twojego zadłużenia w poszczególnych miesiąc przez najbliższe 2 lata")

enter = input('Naciśnij "enter", aby rozpocząć ')

# wyskakuj z informacji

pocz_kredyt = input("1. Podaj początkową wysokość kredytu [PLN]: ")
pocz_kredyt = float(pocz_kredyt)

opr_kredyt = input("2. Podaj oprocentowanie kredytu [%]: ")
opr_kredyt = float(opr_kredyt)

stala_rata = input("3. Podaj stałą wartość raty [PLN]: ")
stala_rata = float(stala_rata)

# Wprowadzone wartości inflacji

I_Sty1 = 1,59
I_Lut1 = -0,45
I_Mar1 = 2,32
I_Kwi1 = 1,26
I_Maj1 = 1,78
I_Cze1 = 2,33
I_Lip1 = 1,50
I_Sie1 = 1,78
I_Wrz1 = 2,33
I_Paz1 = 0,62
I_Lis1 = 2,35
I_Gru1 = 0,34

# Obliczenia dla poszczególnych miesięcy


