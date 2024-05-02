class Client:
    def __init__(self, client_id, name, address, contact, budget):
        self.client_id = client_id
        self.name = name
        self.address = address
        self.contact = contact
        self.budget = budget

    def __str__(self):
        return f"Client ID: {self.client_id}\nName: {self.name}\nAddress: {self.address}\nContact: {self.contact}\nBudget: {self.budget}"
