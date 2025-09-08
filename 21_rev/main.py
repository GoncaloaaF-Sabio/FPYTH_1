"""






 Neste momento o programa deverá ser encerrado,
 exibindo o relatório do dia, que conterá a quantidade e o valor total de prestações pagas no dia.



"""
# Quando houver atraso, cobrar 3% de multa, mais 0,1% de juros por dia de atraso.
def valorPagamento(prestacao, atraso):
    if atraso == 0:
        return prestacao

    juro = (prestacao * 0.001) * atraso

    return (prestacao * 1.03) + juro



total_prest = 0
total_pago = 0

while True:

    perst = float(input("Valor das prestação: "))
    if perst == 0:
        break

    atraso = int(input("dias de atraso: "))

    valor = valorPagamento(perst, atraso)

    print(f"o valor da prestação é: {valor:.2f}")

    total_pago += valor
    total_prest += 1


print(f"foram pagas {total_prest} prestações num total de {total_pago:.2f} UM ")