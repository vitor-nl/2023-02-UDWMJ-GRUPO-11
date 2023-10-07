from nis import cat
from Category import Category

class Product:
    def __init__(self, name, description, date_fabrication, is_active, category : Category):
        self.name = name
        self.description = description
        self.date_fabrication = date_fabrication
        self.is_active = is_active
        self.category = category
