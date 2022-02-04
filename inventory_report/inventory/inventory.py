from inventory_report.reports.simple_report import SimpleReport
from inventory_report.reports.complete_report import CompleteReport
import csv


def read(path):
    with open(path) as file:
        inventory_reader = csv.DictReader(file, delimiter=",", quotechar='"')
        inventories = []
        for inv in inventory_reader:
            inventories.append(inv)
        return inventories


class Inventory:
    def import_data(lista, report):
        read_file = read(lista)
        if report == "simples":
            return SimpleReport.generate(read_file)
        else:
            return CompleteReport.generate(read_file)
