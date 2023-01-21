separador = "=============================================="
lista_vazamentos = [
    ["Adobe", "04", 2022, ["Email", "Telefone", "Nomes", "Senhas", "Dicas de Senhas"]],
    ["Microsoft", "01", 2020, ["Email", "Telefone", "Nomes", "Senhas"]],
    ["Apple", "12", 2010, ["Telefone"]],
    ["IBM", "11", 2009, ["Email"]],
    ["Intel", "10", 2017, ["Email", "Telefone", "Nomes", "Senhas"]],
    ["Dell", "07", 2018, ["Email", "Telefone", "Nomes", "Senhas", "Dicas de Senhas"]],
    ["Mozilla", "11", 2022, ["Email", "Telefone", "Nomes", "Senhas"]],
    ["Google", "12", 2022, ["Email", "Telefone"]],
    ["Itau", "08", 2016, ["Nomes"]],
    ["Nubank", "01", 2021, ["Email", "Telefone", "Nomes", "Senhas"]],
    ["Bradesco", "11", 2018, ["Email", "Telefone", "Senhas"]],
    ["HP", "09", 2011, ["Email", "Telefone", "Nomes", "Senhas"]],
    ["Booking", "10", 2015, ["Nomes", "Senhas", "Dicas de Senhas"]],
    ["GOL", "12", 2014, ["Email", "Telefone", "Nomes", "Senhas"]],
    ["Catho", "08", 2022, ["Nomes", "Senhas"]],
    ["LinkedIn", "11", 2020, ["Email", "Telefone", "Nomes", "Dicas de Senhas"]]
]

mes = int(input("Informe o ano atual: "))
ano = int(input("Informe o mês atual: "))

risco_baixo = ["Nomes"]
risco_medio = ["Email", "Telefone"]
risco_alto = ["Dicas de Senhas"]
risco_altissimo = ["Senhas"]

for vazamento in lista_vazamentos:
    score = 0
    multiplicador = 1
    tempo_vazamento = ano - vazamento[2]

    if tempo_vazamento <= 2:
        multiplicador = 2
        if int(vazamento[2]) == ano:
            if int(vazamento[1]) - mes < 3:
                multiplicador = 3
    elif 2 < tempo_vazamento <= 4:
        multiplicador = 1.2

    for dado_vazado in vazamento[3]:
        if dado_vazado in risco_baixo:
            score += 10
        elif dado_vazado in risco_medio:
            score += 20
        elif dado_vazado in risco_alto:
            score += 80
        elif dado_vazado in risco_altissimo:
            score += 150

    score *= multiplicador

    vazamento.append(score)
    vazamento.append(multiplicador)

for j in range(len(lista_vazamentos) - 1):
    for i in range(len(lista_vazamentos) - 1):
        if lista_vazamentos[i][4] < lista_vazamentos[i + 1][4]:
            lista_vazamentos[i], lista_vazamentos[i + 1] = lista_vazamentos[i + 1], lista_vazamentos[i]

indice = 1
print("{}\n{}\n{}".format(separador, "RELATÓRIO DE RISCO", separador))
for vazamento in lista_vazamentos:
    dados = ""
    for dado in vazamento[3]:
        dados += "{}, ".format(dado)
    print("{}.{} {}/{} \nForam vazados:\n{}\nScore de risco: {}\nMultiplicador de risco: {}\n{}".format(indice, vazamento[0], vazamento[1], vazamento[2], ",\n".join(["{}"]*len(vazamento[3])).format(*vazamento[3]), vazamento[4], vazamento[5], separador))
    indice += 1
