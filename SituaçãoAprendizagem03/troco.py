def calcular_troco(valor_total, valor_recebido):
    troco = valor_recebido - valor_total
    
    notas_moedas = [100, 50, 20, 10, 5, 2, 1, 0.50, 0.25, 0.10, 0.05, 0.01]
    
    troco_notas_moedas = {}

    for nota_moeda in notas_moedas:
        quantidade = int(troco // nota_moeda) 
        if quantidade > 0:
            troco_notas_moedas[nota_moeda] = quantidade
            troco -= quantidade * nota_moeda  

    return troco_notas_moedas


def main():
    valor_total = float(input("Digite o valor total da compra: R$ "))
    valor_recebido = float(input("Digite o valor recebido: R$ "))
    
    troco = calcular_troco(valor_total, valor_recebido)

    if valor_recebido < valor_total:
        print("O valor recebido é menor que o valor total da compra.")
    elif valor_recebido == valor_total:
        print("Nenhum troco necessário.")
    else:
        print("\nTroco a ser devolvido:")
        for nota_moeda, quantidade in troco.items():
            tipo = "Moeda" if nota_moeda < 2 else "Nota"
            print(f"{quantidade} {tipo}(s) de R$ {nota_moeda:.2f}")


if __name__ == "__main__":
    main()
