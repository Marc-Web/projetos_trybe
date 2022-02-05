from inventory_report.importer.importer import Importer
import json


class JsonImporter(Importer):
    def import_data(path):
        type_file = path.split(".")
        if type_file[1] != "json":
            raise ValueError('Arquivo inválido')
        with open(path) as file:
            inventory_reader = json.load(file)
            inventories = []
            for inv in inventory_reader:
                inventories.append(inv)
        return inventories
