
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

I_Sty1 = 1.59
I_Lut1 = -0.45
I_Mar1 = 2.32
I_Kwi1 = 1.26
I_Maj1 = 1.78
I_Cze1 = 2.33
I_Lip1 = 1.50
I_Sie1 = 1.78
I_Wrz1 = 2.33
I_Paz1 = 0.62
I_Lis1 = 2.35
I_Gru1 = 0.34

# Obliczenia dla poszczególnych miesięcy

print("Twoje zadłużenie w poszczególnych miesiącach:")

Sty1 = (1+((I_Sty1 + opr_kredyt)/1200)) * pocz_kredyt - stala_rata
print("Styczeń 2023:", Sty1)

Lut1 = (1+((I_Lut1 + opr_kredyt)/1200)) * Sty1 - stala_rata
print("Luty 2023:", round(Lut1, 2))

Mar1 = (1+((I_Mar1 + opr_kredyt)/1200)) * Lut1 - stala_rata
print("Marzec 2023:", round(Mar1, 2))

Kwi1 = (1+((I_Kwi1 + opr_kredyt)/1200)) * Mar1 - stala_rata
print("Kwiecień 2023:", round(Kwi1, 2))

Maj1 = (1+((I_Maj1 + opr_kredyt)/1200)) * Kwi1 - stala_rata
print("Maj 2023:", round(Maj1, 2))

Cze1 = (1+((I_Cze1 + opr_kredyt)/1200)) * Maj1 - stala_rata
print("Czerwiec 2023:", round(Cze1, 2))

Sie1 = (1+((I_Sie1 + opr_kredyt)/1200)) * Cze1 - stala_rata
print("Sierpień 2023:", round(Sie1, 2))

Wrz1 = (1+((I_Wrz1 + opr_kredyt)/1200)) * Sie1 - stala_rata
print("Wrzesień 2023:", round(Wrz1, 2))

Paz1 = (1+((I_Paz1 + opr_kredyt)/1200)) * Wrz1 - stala_rata
print("Październik 2023:", round(Paz1, 2))

Lis1 = (1+((I_Lis1 + opr_kredyt)/1200)) * Paz1 - stala_rata
print("Listopad 2023:", round(Lis1, 2))

Gru1 = (1+((I_Gru1 + opr_kredyt)/1200)) * Lis1 - stala_rata
print("Grudzień 2023:", round(Gru1, 2))
