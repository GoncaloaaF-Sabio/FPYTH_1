"""
Faça um programa que converta da notação de 24 horas para a notação de 12 horas.

 Por exemplo, o programa deve converter 14:25 em 2:25 P.M.

 A entrada é dada em dois inteiros. - Done

 Deve haver pelo menos duas funções: - Done
        uma para fazer a conversão
        uma para a saída.  - Done

    Registre a informação A.M./P.M. como
        ‘A’/ 'a' para A.M. e
        ‘P’/ 'p' para P.M. ,

Assim a função para efetuar as conversões terá um parâmetro formal para registrar se é A.M. ou P.M.

Inclua um loop que permita que o usr repita esse cálculo para novos valores de entrada todas as vezes que desejar.

"""
num = 112
s = f"num: {num:03d}"
# print(s)


def converter_24_12(horas: int, minutos: int):
    ampm = "A"
    if horas > 12:
        horas = horas - 12
        ampm = "P"

    print(mostrar_conversao(horas, minutos, ampm))


def mostrar_conversao(horas:int, minutos:int, ampm:str):
    if ampm.lower() == 'a':
        ampm = "AM"
    elif ampm.lower() == 'p':
        ampm = "PM"
    else:
         return  "Formato incorreto"

    if horas not in range(1, 13) or minutos not in range(0, 60):
        return "resultado invalido"

    return f"{horas:02d}:{minutos:02d} {ampm}"



def pedir_horas():
    pedir_hora = True
    while pedir_hora:

        hora = int(input("Hora: "))
        minutos = int(input("Minutos: "))

        converter_24_12(hora, minutos)

        novahora = str(input("fazer nova conversão (s/n): "))

        if novahora.lower() == 'n':
            pedir_hora = False




# converter_24_12(18, 12)

pedir_horas()




