from inventory_report.reports.simple_report import SimpleReport


def companys_stock(lista):
    companys = []
    for item in lista:
        companys.append(item["nome_da_empresa"])
    companys_string = ""
    for company in companys:
        if company not in companys_string:
            companys_string += f"- {company}: {companys.count(company)}\n"
    return companys_string


class CompleteReport(SimpleReport):
    def generate(lista):
        return (
            SimpleReport.generate(lista)
            + "\n"
            + "Produtos estocados por empresa: \n"
            + companys_stock(lista)
        )
