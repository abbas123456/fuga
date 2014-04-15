from adaptor import model, fields
from mobile_products import models


class MobileProductModel(model.XMLModel):
    multiple_creation_field = False
    
    class Meta:
        dbModel = models.MobileProduct

    root = fields.XMLRootField(path="/mobile_product")
    notes = fields.XMLCharField(path="mobile_product_notes")
