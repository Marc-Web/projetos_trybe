from inventory_report.importer.importer import Importer
import csv


class CsvImporter(Importer):
    def import_data(path):
        type_file = path.split(".")
        if type_file[1] != "csv":
            raise ValueError('Arquivo inválido')
        with open(path) as file:
            inventory_reader = csv.DictReader(
                file, delimiter=",", quotechar='"'
            )
            inventories = []
            for inv in inventory_reader:
                inventories.append(inv)
        return inventories
