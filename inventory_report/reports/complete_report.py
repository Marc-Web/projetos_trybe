from inventory_report.reports.simple_report import SimpleReport
from typing import Counter


def companys_stock(lista):
    companys = []
    for item in lista:
        companys.append(item["nome_da_empresa"])
    # https://pt.stackoverflow.com/questions/456224/obter-o-elemento-mais-frequente-e-menos-frequente-de-uma-lista-al%C3%A9m-do-maior-e
    more_frequent = Counter(companys).most_common()
    print(more_frequent)
    return (
        "Produtos estocados por empresa: \n"
        f"- {more_frequent[1][0]}: {more_frequent[1][1]}\n"
        f"- {more_frequent[0][0]}: {more_frequent[0][1]}\n"
        f"- {more_frequent[2][0]}: {more_frequent[2][1]}\n"
    )


class CompleteReport(SimpleReport):
    def generate(lista):
        return SimpleReport.generate(lista) + "\n" + companys_stock(lista)
