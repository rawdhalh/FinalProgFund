class Guest:
    def __init__(self, guest_id, name, address, contact):
        self.guest_id = guest_id
        self.name = name
        self.address = address
        self.contact = contact
    
    def __str__(self):
        return f"Guest ID: {self.guest_id}\nName: {self.name}\nAddress: {self.address}\nContact: {self.contact}"
