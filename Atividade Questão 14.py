dias =  int (input ("Digite o(s) Dia(s) "))
horas =  int (input ("Digite a(s) Hora(s) "))
minutos =  int (input ("Digite o(s) Minuto(s) "))
segundos =  int (input ("Digite o(s) Segundo(s) "))

total = (((dias * 24 + horas) * 60 + minutos) * 60 + segundos)

print("vai dar um total de ",total, "segundos")
