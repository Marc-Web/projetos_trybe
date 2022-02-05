from inventory_report.reports.simple_report import SimpleReport
from inventory_report.reports.complete_report import CompleteReport
from inventory_report.importer.csv_importer import CsvImporter
from inventory_report.importer.json_importer import JsonImporter
from inventory_report.importer.xml_importer import XmlImporter


def read(path):
    type_file = path.split(".")
    if type_file[1] == "csv":
        return CsvImporter.import_data(path)
    elif type_file[1] == "json":
        return JsonImporter.import_data(path)
    elif type_file[1] == "xml":
        return XmlImporter.import_data(path)


class Inventory:
    def import_data(lista, report):
        read_file = read(lista)
        if report == "simples":
            return SimpleReport.generate(read_file)
        else:
            return CompleteReport.generate(read_file)
