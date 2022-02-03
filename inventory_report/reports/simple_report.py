from datetime import date
from typing import Counter


def oldest_manufacturing_date(lista):
    oldest = lista[0]["data_de_fabricacao"]
    for item in lista:
        if item["data_de_fabricacao"] < oldest:
            oldest = item["data_de_fabricacao"]
    return oldest


def closest_expiration_date(lista):
    today_date = date.today().strftime("%Y-%m-%d")
    closest = lista[0]["data_de_validade"]
    for item in lista:
        if (
            item["data_de_validade"] < closest
            and item["data_de_validade"] > today_date
        ):
            closest = item["data_de_validade"]
    return closest


def company_largest_stock(lista):
    companys = []
    for item in lista:
        companys.append(item["nome_da_empresa"])
    # https://pt.stackoverflow.com/questions/456224/obter-o-elemento-mais-frequente-e-menos-frequente-de-uma-lista-al%C3%A9m-do-maior-e
    more_frequent = Counter(companys).most_common()
    return more_frequent[0][0]


class SimpleReport:
    def generate(lista):
        oldest = oldest_manufacturing_date(lista)
        closest = closest_expiration_date(lista)
        company = company_largest_stock(lista)
        return (
            f"Data de fabricação mais antiga: {oldest}\n"
            f"Data de validade mais próxima: {closest}\n"
            f"Empresa com maior quantidade de produtos estocados: {company}\n"
        )
