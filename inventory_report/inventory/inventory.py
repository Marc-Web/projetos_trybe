from inventory_report.reports.simple_report import SimpleReport
from inventory_report.reports.complete_report import CompleteReport
import csv
import json
import xmltodict


def read_CSV(path):
    with open(path) as file:
        inventory_reader = csv.DictReader(file, delimiter=",", quotechar='"')
        inventories = []
        for inv in inventory_reader:
            inventories.append(inv)
    return inventories


def read_JSON(path):
    with open(path) as file:
        inventory_reader = json.load(file)
        inventories = []
        for inv in inventory_reader:
            inventories.append(inv)
    return inventories


def read_XML(path):
    with open(path) as file:
        read_file = file.read()
        convert_to_dict = xmltodict.parse(read_file)
        inventories = convert_to_dict["dataset"]["record"]
    return inventories


def read(path):
    type_file = path.split(".")
    if type_file[1] == "csv":
        return read_CSV(path)
    elif type_file[1] == "json":
        return read_JSON(path)
    elif type_file[1] == "xml":
        return read_XML(path)


class Inventory:
    def import_data(lista, report):
        read_file = read(lista)
        if report == "simples":
            return SimpleReport.generate(read_file)
        else:
            return CompleteReport.generate(read_file)
