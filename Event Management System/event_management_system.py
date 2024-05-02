import pickle
from tkinter import messagebox

class EventManagementSystem:
    def __init__(self):
        self.employees = []
        self.events = []
        self.clients = []
        self.guests = []
        self.suppliers = []
        self.load_employee_data()
        self.load_client_data()
        self.load_guest_data()
        self.load_supplier_data()
        self.load_event_data()

    # Employee - Event Management System
    def save_employee_data(self):
        with open("employees.pkl", 'wb') as file:
            pickle.dump(self.employees, file)

    def load_employee_data(self):
        try:
            with open("employees.pkl", 'rb') as file:
                self.employees = pickle.load(file)
        except FileNotFoundError:
            self.employees = []

    def add_employee(self, employee):
        self.employees.append(employee)
        self.save_employee_data()

    def delete_employee(self, employee_id):
        employee_id = int(employee_id)
        employee_found = False
        for employee in self.employees:
            if employee.id == employee_id:
                self.employees.remove(employee)
                self.save_employee_data()
                employee_found = True
                break
        
        if employee_found:
            messagebox.showinfo("Success", "Employee deleted successfully!")
        else:
            messagebox.showerror("Error", "Employee not found with ID {}".format(employee_id))


    def employee_exits(self, employee_id):
        employee_id = int(employee_id)
        employee_found = False
        for employee in self.employees:
            if employee.id == employee_id:
                employee_found = True
        return employee_found
    
    def modify_employee(self, employee_id, new_employee):
        employee_id = int(employee_id)
        employee_found = False
        for employee in self.employees:
            if employee.id == employee_id:
                employee.name = new_employee.name
                employee.department = new_employee.department
                employee.job_title = new_employee.job_title
                employee.basic_salary = new_employee.basic_salary
                employee.age = new_employee.age
                employee.date_of_birth = new_employee.date_of_birth
                employee.passport_details = new_employee.passport_details
                employee_found = True
                self.save_employee_data()
                break
        
        if employee_found:
            messagebox.showinfo("Success", "Employee details modified successfully!")
        else:
            messagebox.showerror("Error", "Employee not found with ID {}".format(employee_id))


    def display_employee(self, employee_id):
        employee_id = int(employee_id)
        for employee in self.employees:
            if employee.id == employee_id:
                return employee


    # Client - Event Management System
    def save_client_data(self):
        with open("clients.pkl", 'wb') as file:
            pickle.dump(self.clients, file)

    def load_client_data(self):
        try:
            with open("clients.pkl", 'rb') as file:
                self.clients = pickle.load(file)
        except FileNotFoundError:
            self.clients = []
    
    def add_client(self, client):
        self.clients.append(client)
        self.save_client_data()

    def delete_client(self, client_id):
        client_id = int(client_id)
        client_found = False
        for client in self.clients:
            if client.client_id == client_id:
                self.clients.remove(client)
                self.save_client_data()
                client_found = True
                break
        
        if client_found:
            messagebox.showinfo("Success", "Client deleted successfully!")
        else:
            messagebox.showerror("Error", "Client not found with ID {}".format(client_id))

    def client_exists(self, client_id):
        client_id = int(client_id)
        client_found = False
        for client in self.clients:
            if client.client_id == client_id:
                client_found = True
                break
        return client_found
    
    def modify_client(self, client_id, new_client):
        client_id = int(client_id)
        client_found = False
        for client in self.clients:
            if client.client_id == client_id:
                client.name = new_client.name
                client.address = new_client.address
                client.contact = new_client.contact
                client.budget = new_client.budget
                client_found = True
                self.save_client_data()
                break
        
        if client_found:
            messagebox.showinfo("Success", "Client details modified successfully!")
        else:
            messagebox.showerror("Error", "Client not found with ID {}".format(client_id))

    def display_client(self, client_id):
        client_id = int(client_id)
        for client in self.clients:
            if client.client_id == client_id:
                return client


    # Guest - Event Management System
    def save_guest_data(self):
        with open("guests.pkl", 'wb') as file:
            pickle.dump(self.guests, file)

    def load_guest_data(self):
        try:
            with open("guests.pkl", 'rb') as file:
                self.guests = pickle.load(file)
        except FileNotFoundError:
            self.guests = []

    def add_guest(self, guest):
        self.guests.append(guest)
        self.save_guest_data()

    def delete_guest(self, guest_id):
        guest_id = int(guest_id)
        guest_found = False
        for guest in self.guests:
            if guest.guest_id == guest_id:
                self.guests.remove(guest)
                self.save_guest_data()
                guest_found = True
                break
        
        if guest_found:
            messagebox.showinfo("Success", "Guest deleted successfully!")
        else:
            messagebox.showerror("Error", "Guest not found with ID {}".format(guest_id))

    def guest_exists(self, guest_id):
        guest_id = int(guest_id)
        guest_found = False
        for guest in self.guests:
            if guest.guest_id == guest_id:
                guest_found = True
                break
        return guest_found
    
    def modify_guest(self, guest_id, new_guest):
        guest_id = int(guest_id)
        guest_found = False
        for guest in self.guests:
            if guest.guest_id == guest_id:
                guest.name = new_guest.name
                guest.address = new_guest.address
                guest.contact = new_guest.contact
                guest_found = True
                self.save_guest_data()
                break
        
        if guest_found:
            messagebox.showinfo("Success", "Guest details modified successfully!")
        else:
            messagebox.showerror("Error", "Guest not found with ID {}".format(guest_id))

    def display_guest(self, guest_id):
        guest_id = int(guest_id)
        for guest in self.guests:
            if guest.guest_id == guest_id:
                return guest

    # Suppliers - Event Management System
    def save_supplier_data(self):
        with open("suppliers.pkl", 'wb') as file:
            pickle.dump(self.suppliers, file)

    def load_supplier_data(self):
        try:
            with open("suppliers.pkl", 'rb') as file:
                self.suppliers = pickle.load(file)
        except FileNotFoundError:
            self.suppliers = []

    def add_supplier(self, supplier):
        self.suppliers.append(supplier)
        self.save_supplier_data()

    def delete_supplier(self, supplier_id):
        supplier_id = int(supplier_id)
        supplier_found = False
        for supplier in self.suppliers:
            if supplier.supplier_id == supplier_id:
                self.suppliers.remove(supplier)
                self.save_supplier_data()
                supplier_found = True
                break
        
        if supplier_found:
            messagebox.showinfo("Success", "Supplier deleted successfully!")
        else:
            messagebox.showerror("Error", "Supplier not found with ID {}".format(supplier_id))

    def supplier_exists(self, supplier_id):
        supplier_id = int(supplier_id)
        supplier_found = False
        for supplier in self.suppliers:
            if supplier.supplier_id == supplier_id:
                supplier_found = True
                break
        return supplier_found
    
    def modify_supplier(self, supplier_id, new_supplier):
        supplier_id = int(supplier_id)
        supplier_found = False
        for supplier in self.suppliers:
            if supplier.supplier_id == supplier_id:
                supplier.name = new_supplier.name
                supplier.address = new_supplier.address
                supplier.contact = new_supplier.contact
                supplier.supplier_type = new_supplier.supplier_type
                supplier_found = True
                self.save_supplier_data()
                break
        
        if supplier_found:
            messagebox.showinfo("Success", "Supplier details modified successfully!")
        else:
            messagebox.showerror("Error", "Supplier not found with ID {}".format(supplier_id))


    def display_supplier(self, supplier_id):
        supplier_id = int(supplier_id)
        for supplier in self.suppliers:
            if supplier.supplier_id == supplier_id:
                return supplier


    # Event - Event Management System
    def save_event_data(self):
        with open("events.pkl", 'wb') as file:
            pickle.dump(self.events, file)

    def load_event_data(self):
        try:
            with open("events.pkl", 'rb') as file:
                self.events = pickle.load(file)
        except FileNotFoundError:
            self.events = []

    def add_event(self, event):
        self.events.append(event)
        self.save_event_data()

    def delete_event(self, event_id):
        event_id = int(event_id)
        event_found = False
        for event in self.events:
            if event.event_id == event_id:
                self.events.remove(event)
                self.save_event_data()
                event_found = True
                break
        
        if event_found:
            messagebox.showinfo("Success", "Event deleted successfully!")
        else:
            messagebox.showerror("Error", "Event not found with ID {}".format(event_id))

    def event_exists(self, event_id):
        event_id = int(event_id)
        event_found = False
        for event in self.events:
            if event.event_id == event_id:
                event_found = True
                break
        return event_found
    
    def modify_event(self, event_id, new_event):
        event_id = int(event_id)
        event_found = False
        for event in self.events:
            if event.event_id == event_id:
                event.event_type = new_event.event_type
                event.theme = new_event.theme
                event.date = new_event.date
                event.time = new_event.time
                event.duration = new_event.duration
                event.venue_address = new_event.venue_address
                event.client_id = new_event.client_id
                event.guest_list = new_event.guest_list
                event.catering_company = new_event.catering_company
                event.cleaning_company = new_event.cleaning_company
                event.decorations_company = new_event.decorations_company
                event.entertainment_company = new_event.entertainment_company
                event.furniture_company = new_event.furniture_company
                event.invoice = new_event.invoice
                event_found = True
                self.save_event_data()
                break
        
        if event_found:
            messagebox.showinfo("Success", "Event details modified successfully!")
        else:
            messagebox.showerror("Error", "Event not found with ID {}".format(event_id))


    def display_event(self, event_id):
        event_id = int(event_id)
        for event in self.events:
            if event.event_id == event_id:
                return event