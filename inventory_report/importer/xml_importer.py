from inventory_report.importer.importer import Importer
import xmltodict


class XmlImporter(Importer):
    def import_data(path):
        type_file = path.split(".")
        if type_file[1] != "xml":
            raise ValueError('Arquivo inválido')
        with open(path) as file:
            read_file = file.read()
            convert_to_dict = xmltodict.parse(read_file)
            inventories = convert_to_dict["dataset"]["record"]
        return inventories
