class Supplier:
    def __init__(self, supplier_id, name, address, contact, supplier_type):
        self.supplier_id = supplier_id
        self.name = name
        self.address = address
        self.contact = contact
        self.supplier_type = supplier_type
    
    def __str__(self):
        return f"Supplier ID: {self.supplier_id}\nName: {self.name}\nAddress: {self.address}\nContact: {self.contact}\nType: {self.supplier_type}"
