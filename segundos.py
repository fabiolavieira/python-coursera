segundos = int(input("Por favor, entre com o número de segundos que deseja converter: "))

dias = segundos // 86400
seg_rest = segundos % 86400
horas = seg_rest // 3600
seg_rest = seg_rest % 3600
minutos = seg_rest // 60
segundos = seg_rest % 60

print(dias, "dias,", horas, "horas,", minutos, "minutos e", segundos, "segundos.")
