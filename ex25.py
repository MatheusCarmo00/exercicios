hora_inicio = int(input("Hora de início: "))
minuto_inicio = int(input("Minuto de início: "))

hora_fim = int(input("Hora de término: "))
minuto_fim = int(input("Minuto de término: "))

inicio = hora_inicio * 60 + minuto_inicio
fim = hora_fim * 60 + minuto_fim

if fim <= inicio:
    fim += 24 * 60

duracao = fim - inicio

horas = duracao // 60
minutos = duracao % 60

print("Duração:", horas, "hora(s) e", minutos, "minuto(s)")