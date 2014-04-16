import os.path

from django.core.management.base import BaseCommand, CommandError
from lxml import etree

from mobile_products.xml_adaptor import MobileProductModel


class Command(BaseCommand):
    args = "<xml_filename>"
    help = ("Imports a mobile_products xml file and creates the "
            "approprirate models")
    XSD_FILENAME = "mobile_products/integration/fuga_delivery_mobile_product-1.4.4.xsd"

    def handle(self, *args, **options):
        if (len(args) == 0):
            raise CommandError("Arguments are <xml_filename>")
        xml_filename = args[0]

        if (not os.path.isfile(xml_filename)):
            raise CommandError("File does not exist")

        xml_valid, errors = self._validate_xml_using_xsd(xml_filename)

        if (xml_valid):
            try:
                xml_file_data = open(xml_filename).read()
                model = MobileProductModel.import_data(data=xml_file_data)[0]
                model.create_model_instance(model.as_dict())
            except:
                raise CommandError("Something went wrong during the import")
        else:
            raise CommandError("The XML contains the following errors: %s",
                               errors)

    def _validate_xml_using_xsd(self, xml_filename):
        xsd_doc = etree.parse(self.XSD_FILENAME)
        xsd = etree.XMLSchema(xsd_doc)
        xml = etree.parse(xml_filename)
        return xsd.validate(xml), xsd.error_log
