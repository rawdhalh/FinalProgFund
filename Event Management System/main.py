import tkinter as tk
from tkinter import messagebox
import pickle
from employee import Employee
from clients import Client
from guests import Guest
from suppliers import Supplier
from events import Event
from event_management_system import EventManagementSystem


class MainApplication(tk.Tk):
    def __init__(self, system):
        super().__init__()
        self.title("Event Management System")
        self.system = system
        self.create_gui()

    def create_gui(self):
        # Menu
        self.menu = tk.Menu(self)
        self.config(menu=self.menu)

        # Employee Menu
        self.employee_menu = tk.Menu(self.menu, tearoff=0)
        self.employee_menu.add_command(label="Add Employee", command=self.show_add_employee)
        self.employee_menu.add_command(label="Delete Employee", command=self.show_delete_employee)
        self.employee_menu.add_command(label="Modify Employee", command=self.show_modify_employee)
        self.employee_menu.add_command(label="Display Employee Details", command=self.show_display_employee)
        self.menu.add_cascade(label="Employee", menu=self.employee_menu)

         # Client Menu
        self.client_menu = tk.Menu(self.menu, tearoff=0)
        self.client_menu.add_command(label="Add Client", command=self.show_add_client)
        self.client_menu.add_command(label="Delete Client", command=self.show_delete_client)
        self.client_menu.add_command(label="Modify Client", command=self.show_modify_client)
        self.client_menu.add_command(label="Display Client Details", command=self.show_display_client)
        self.menu.add_cascade(label="Client", menu=self.client_menu)

        # Guest Menu
        self.guest_menu = tk.Menu(self.menu, tearoff=0)
        self.guest_menu.add_command(label="Add Guest", command=self.show_add_guest)
        self.guest_menu.add_command(label="Delete Guest", command=self.show_delete_guest)
        self.guest_menu.add_command(label="Modify Guest", command=self.show_modify_guest)
        self.guest_menu.add_command(label="Display Guest Details", command=self.show_display_guest)
        self.menu.add_cascade(label="Guest", menu=self.guest_menu)

        # Supplier Menu
        self.supplier_menu = tk.Menu(self.menu, tearoff=0)
        self.supplier_menu.add_command(label="Add Supplier", command=self.show_add_supplier)
        self.supplier_menu.add_command(label="Delete Supplier", command=self.show_delete_supplier)
        self.supplier_menu.add_command(label="Modify Supplier", command=self.show_modify_supplier)
        self.supplier_menu.add_command(label="Display Supplier Details", command=self.show_display_supplier)
        self.menu.add_cascade(label="Supplier", menu=self.supplier_menu)

        # Event Menu
        self.event_menu = tk.Menu(self.menu, tearoff=0)
        self.event_menu.add_command(label="Add Event", command=self.show_add_event)
        self.event_menu.add_command(label="Delete Event", command=self.show_delete_event)
        self.event_menu.add_command(label="Modify Event", command=self.show_modify_event)
        self.event_menu.add_command(label="Display Event Details", command=self.show_display_event)
        self.menu.add_cascade(label="Event", menu=self.event_menu)

        # Frames
        self.frame = tk.Frame(self)
        self.frame.pack()

        # Entry fields for adding employee
        self.id_entry = tk.Entry(self.frame)
        self.name_entry = tk.Entry(self.frame)
        self.department_entry = tk.Entry(self.frame)
        self.job_title_entry = tk.Entry(self.frame)
        self.basic_salary_entry = tk.Entry(self.frame)
        self.age_entry = tk.Entry(self.frame)
        self.date_of_birth_entry = tk.Entry(self.frame)
        self.passport_details_entry = tk.Entry(self.frame)
        self.manager_id_entry = tk.Entry(self.frame)

        # Entry fields for adding client
        self.client_id_entry = tk.Entry(self.frame)
        self.name_entry = tk.Entry(self.frame)
        self.address_entry = tk.Entry(self.frame)
        self.contact_entry = tk.Entry(self.frame)
        self.budget_entry = tk.Entry(self.frame)


        # Entry fields for modifying employee
        self.modify_id_entry = tk.Entry(self.frame)
        self.new_name_entry = tk.Entry(self.frame)
        self.new_department_entry = tk.Entry(self.frame)
        self.new_job_title_entry = tk.Entry(self.frame)
        self.new_basic_salary_entry = tk.Entry(self.frame)
        self.new_age_entry = tk.Entry(self.frame)
        self.new_date_of_birth_entry = tk.Entry(self.frame)
        self.new_passport_details_entry = tk.Entry(self.frame)
        self.new_manager_id_entry = tk.Entry(self.frame)

        # Entry fields for modifying client
        self.modify_client_id_entry = tk.Entry(self.frame)
        self.new_name_entry = tk.Entry(self.frame)
        self.new_address_entry = tk.Entry(self.frame)
        self.new_contact_entry = tk.Entry(self.frame)
        self.new_budget_entry = tk.Entry(self.frame)

        # Entry fields for adding guest
        self.id_entry = tk.Entry(self.frame)
        self.name_entry = tk.Entry(self.frame)
        self.address_entry = tk.Entry(self.frame)
        self.contact_entry = tk.Entry(self.frame)

        # Entry fields for modifying guest
        self.modify_id_entry = tk.Entry(self.frame)
        self.new_name_entry = tk.Entry(self.frame)
        self.new_address_entry = tk.Entry(self.frame)
        self.new_contact_entry = tk.Entry(self.frame)

        # Entry fields for adding supplier
        self.supplier_id_entry = tk.Entry(self.frame)
        self.name_entry = tk.Entry(self.frame)
        self.address_entry = tk.Entry(self.frame)
        self.contact_entry = tk.Entry(self.frame)
        self.supplier_type_entry = tk.Entry(self.frame)

        # Entry fields for modifying supplier
        self.modify_supplier_id_entry = tk.Entry(self.frame)
        self.new_name_entry = tk.Entry(self.frame)
        self.new_address_entry = tk.Entry(self.frame)
        self.new_contact_entry = tk.Entry(self.frame)
        self.new_supplier_type_entry = tk.Entry(self.frame)

        # Entry fields for adding event
        self.event_id_entry = tk.Entry(self.frame)
        self.event_type_entry = tk.Entry(self.frame)
        self.theme_entry = tk.Entry(self.frame)
        self.date_entry = tk.Entry(self.frame)
        self.time_entry = tk.Entry(self.frame)
        self.duration_entry = tk.Entry(self.frame)
        self.venue_address_entry = tk.Entry(self.frame)
        self.client_id_entry = tk.Entry(self.frame)
        self.guest_list_entry = tk.Entry(self.frame)
        self.catering_company_entry = tk.Entry(self.frame)
        self.cleaning_company_entry = tk.Entry(self.frame)
        self.decorations_company_entry = tk.Entry(self.frame)
        self.entertainment_company_entry = tk.Entry(self.frame)
        self.furniture_company_entry = tk.Entry(self.frame)
        self.invoice_entry = tk.Entry(self.frame)

        # Entry fields for modifying event
        self.modify_event_id_entry = tk.Entry(self.frame)
        self.new_event_type_entry = tk.Entry(self.frame)
        self.new_theme_entry = tk.Entry(self.frame)
        self.new_date_entry = tk.Entry(self.frame)
        self.new_time_entry = tk.Entry(self.frame)
        self.new_duration_entry = tk.Entry(self.frame)
        self.new_venue_address_entry = tk.Entry(self.frame)
        self.new_client_id_entry = tk.Entry(self.frame)
        self.new_guest_list_entry = tk.Entry(self.frame)
        self.new_catering_company_entry = tk.Entry(self.frame)
        self.new_cleaning_company_entry = tk.Entry(self.frame)
        self.new_decorations_company_entry = tk.Entry(self.frame)
        self.new_entertainment_company_entry = tk.Entry(self.frame)
        self.new_furniture_company_entry = tk.Entry(self.frame)
        self.new_invoice_entry = tk.Entry(self.frame)

    def clear_frame(self):
        for widget in self.frame.winfo_children():
            widget.destroy()

    # Employee Crud GUI
    def show_add_employee(self):
        self.clear_frame()
        tk.Label(self.frame, text="Add Employee").grid(row=0, column=0, columnspan=2, pady=10)

        tk.Label(self.frame, text="ID:").grid(row=1, column=0)
        self.id_entry = tk.Entry(self.frame)
        self.id_entry.grid(row=1, column=1)

        tk.Label(self.frame, text="Name:").grid(row=2, column=0)
        self.name_entry = tk.Entry(self.frame)
        self.name_entry.grid(row=2, column=1)

        tk.Label(self.frame, text="Department:").grid(row=3, column=0)
        self.department_entry = tk.Entry(self.frame)
        self.department_entry.grid(row=3, column=1)

        tk.Label(self.frame, text="Job Title:").grid(row=4, column=0)
        self.job_title_entry = tk.Entry(self.frame)
        self.job_title_entry.grid(row=4, column=1)

        tk.Label(self.frame, text="Basic Salary:").grid(row=5, column=0)
        self.basic_salary_entry = tk.Entry(self.frame)
        self.basic_salary_entry.grid(row=5, column=1)

        tk.Label(self.frame, text="Age:").grid(row=6, column=0)
        self.age_entry = tk.Entry(self.frame)
        self.age_entry.grid(row=6, column=1)

        tk.Label(self.frame, text="Date of Birth:").grid(row=7, column=0)
        self.date_of_birth_entry = tk.Entry(self.frame)
        self.date_of_birth_entry.grid(row=7, column=1)

        tk.Label(self.frame, text="Passport Details:").grid(row=8, column=0)
        self.passport_details_entry = tk.Entry(self.frame)
        self.passport_details_entry.grid(row=8, column=1)

        tk.Label(self.frame, text="Manager ID:").grid(row=9, column=0)
        self.manager_id_entry = tk.Entry(self.frame)
        self.manager_id_entry.grid(row=9, column=1)

        add_button = tk.Button(self.frame, text="Add", command=self.add_employee)
        add_button.grid(row=10, column=0, columnspan=2, pady=10)

    def show_delete_employee(self):
        self.clear_frame()
        tk.Label(self.frame, text="Delete Employee").grid(row=0, column=0, columnspan=2, pady=10)

        tk.Label(self.frame, text="Employee ID:").grid(row=1, column=0)
        self.delete_id_entry = tk.Entry(self.frame)
        self.delete_id_entry.grid(row=1, column=1)

        delete_button = tk.Button(self.frame, text="Delete", command=self.delete_employee)
        delete_button.grid(row=2, column=0, columnspan=2, pady=10)

    def show_modify_employee(self):
        self.clear_frame()
        tk.Label(self.frame, text="Modify Employee").grid(row=0, column=0, columnspan=2, pady=10)

        tk.Label(self.frame, text="Employee ID:").grid(row=1, column=0)
        self.modify_id_entry = tk.Entry(self.frame)
        self.modify_id_entry.grid(row=1, column=1)

        tk.Label(self.frame, text="New Name:").grid(row=2, column=0)
        self.new_name_entry = tk.Entry(self.frame)
        self.new_name_entry.grid(row=2, column=1)

        tk.Label(self.frame, text="New Department:").grid(row=3, column=0)
        self.new_department_entry = tk.Entry(self.frame)
        self.new_department_entry.grid(row=3, column=1)

        tk.Label(self.frame, text="New Job Title:").grid(row=4, column=0)
        self.new_job_title_entry = tk.Entry(self.frame)
        self.new_job_title_entry.grid(row=4, column=1)

        tk.Label(self.frame, text="New Basic Salary:").grid(row=5, column=0)
        self.new_basic_salary_entry = tk.Entry(self.frame)
        self.new_basic_salary_entry.grid(row=5, column=1)

        tk.Label(self.frame, text="New Age:").grid(row=6, column=0)
        self.new_age_entry = tk.Entry(self.frame)
        self.new_age_entry.grid(row=6, column=1)

        tk.Label(self.frame, text="New Date of Birth:").grid(row=7, column=0)
        self.new_date_of_birth_entry = tk.Entry(self.frame)
        self.new_date_of_birth_entry.grid(row=7, column=1)

        tk.Label(self.frame, text="New Passport Details:").grid(row=8, column=0)
        self.new_passport_details_entry = tk.Entry(self.frame)
        self.new_passport_details_entry.grid(row=8, column=1)

        tk.Label(self.frame, text="New Manager ID:").grid(row=9, column=0)
        self.new_manager_id_entry = tk.Entry(self.frame)
        self.new_manager_id_entry.grid(row=9, column=1)

        modify_button = tk.Button(self.frame, text="Modify", command=self.modify_employee)
        modify_button.grid(row=10, column=0, columnspan=2, pady=10)

    def show_display_employee(self):
        self.clear_frame()
        tk.Label(self.frame, text="Display Employee Details").grid(row=0, column=0, columnspan=2, pady=10)

        tk.Label(self.frame, text="Employee ID:").grid(row=1, column=0)
        self.display_id_entry = tk.Entry(self.frame)
        self.display_id_entry.grid(row=1, column=1)

        display_button = tk.Button(self.frame, text="Display", command=self.display_employee)
        display_button.grid(row=2, column=0, columnspan=2, pady=10)

    def add_employee(self):
        # Fetch values from entry fields
        id_str = self.id_entry.get().strip()
        name = self.name_entry.get().strip()
        department = self.department_entry.get().strip()
        job_title = self.job_title_entry.get().strip()
        basic_salary_str = self.basic_salary_entry.get().strip()
        age_str = self.age_entry.get().strip()
        date_of_birth = self.date_of_birth_entry.get().strip()
        passport_details = self.passport_details_entry.get().strip()
        manager_id = self.manager_id_entry.get().strip()

        # Perform validation
        if not all([id_str, name, department, job_title, basic_salary_str, age_str, date_of_birth, passport_details]):
            # If any required field is empty, show an error message
            messagebox.showerror("Error", "Please provide all required information.")
            return

        try:
            # Convert ID to integer
            employee_id = int(id_str)

            if employee_id <= 0:
                raise ValueError("Employee ID must be a non-negative integer and zero.")

            # Convert basic salary to float
            basic_salary = float(basic_salary_str)

            if basic_salary <= 0:
                raise ValueError("Basic salary must be a positive number.")

            # Convert age to integer
            age = int(age_str)

            if age <= 0:
                raise ValueError("Age must be a posiitive number.")

            # Create an Employee object and add it to the system
            employee = Employee(employee_id, name, department, job_title, basic_salary, age, date_of_birth, passport_details, manager_id)
            # Add employee to system
            self.system.add_employee(employee)
            messagebox.showinfo("Success", "Employee added successfully!")
            # Clear entry fields after adding employee
            self.clear_add_entry_fields()

        except ValueError as ve:
            # Handle specific validation errors
            messagebox.showerror("Error", str(ve))
        except Exception as e:
            # Handle other exceptions
            messagebox.showerror("Error", f"An error occurred: {str(e)}")


    def delete_employee(self):
        # Fetch employee ID from entry field
        employee_id = self.delete_id_entry.get()

        # Delete employee from the system
        self.system.delete_employee(employee_id)
        # messagebox.showinfo("Success", "Employee deleted successfully!")

        # Clear entry field after deleting employee
        self.delete_id_entry.delete(0, tk.END)

    def modify_employee(self):
        
        # Fetch employee ID from entry field
        employee_id = self.modify_id_entry.get().strip()
        # Fetch new details from entry fields
        new_name = self.new_name_entry.get().strip()
        new_department = self.new_department_entry.get().strip()
        new_job_title = self.new_job_title_entry.get().strip()
        new_basic_salary_str = self.new_basic_salary_entry.get().strip()
        new_age_str = self.new_age_entry.get().strip()
        new_date_of_birth = self.new_date_of_birth_entry.get().strip()
        new_passport_details = self.new_passport_details_entry.get().strip()
        new_manager_id = self.new_manager_id_entry.get().strip()

        if self.system.employee_exits(employee_id):
            # Perform validation
            if (new_name == "" or new_department == "" or new_job_title == "" or new_basic_salary_str == "" or
                    new_age_str == "" or new_date_of_birth == "" or new_passport_details == ""):
                # If any required field is empty, show an error message
                messagebox.showerror("Error", "Please provide all required information.")
                return

            try:
                # Convert basic salary to float
                new_basic_salary = float(new_basic_salary_str)

                if new_basic_salary <= 0:
                    raise ValueError("Basic salary must be a positive number.")

                # Convert age to integer
                new_age = int(new_age_str)

                if new_age <= 0:
                    raise ValueError("Age must be a positive number.")

                # Create a new Employee object with updated details
                updated_employee = Employee(employee_id, new_name, new_department, new_job_title, new_basic_salary,
                                            new_age, new_date_of_birth, new_passport_details, new_manager_id)
                # Modify employee details in the system
                self.system.modify_employee(employee_id, updated_employee)
                # Clear entry fields after modifying employee
                self.clear_update_entry_fields()

            except ValueError as ve:
                # Handle specific validation errors
                messagebox.showerror("Error", str(ve))
            except Exception as e:
                # Handle other exceptions
                messagebox.showerror("Error", f"An error occurred: {str(e)}")
        
        else:
            messagebox.showerror("Error", "Employee not found with ID {}".format(employee_id))



    def display_employee(self):
        # Fetch employee ID from entry field
        employee_id = self.display_id_entry.get()

        # Fetch employee details from the system
        employee = self.system.display_employee(employee_id)

        # Display employee details (or perform any action as required)
        if employee:
            messagebox.showinfo("Employee Details", f"Name: {employee.name}\nDepartment: {employee.department}\n"
                                                    f"Job Title: {employee.job_title}\nBasic Salary: {employee.basic_salary}\n"
                                                    f"Age: {employee.age}\nDate of Birth: {employee.date_of_birth}\n"
                                                    f"Passport Details: {employee.passport_details}\n"
                                                    f"Manager ID: {employee.manager_id}")
        else:
            messagebox.showerror("Error", f"Employee not found with ID {employee_id}")


        # Clear entry field after displaying employee details
        self.display_id_entry.delete(0, tk.END)

    def clear_update_entry_fields(self):
        # Clear all entry fields after an operation
        self.modify_id_entry.delete(0, tk.END)
        self.new_name_entry.delete(0, tk.END)
        self.new_department_entry.delete(0, tk.END)
        self.new_job_title_entry.delete(0, tk.END)
        self.new_basic_salary_entry.delete(0, tk.END)
        self.new_age_entry.delete(0, tk.END)
        self.new_date_of_birth_entry.delete(0, tk.END)
        self.new_passport_details_entry.delete(0, tk.END)
        self.new_manager_id_entry.delete(0, tk.END)

    def clear_add_entry_fields(self):
        # Clear all entry fields after an operation
        self.id_entry.delete(0, tk.END)
        self.name_entry.delete(0, tk.END)
        self.department_entry.delete(0, tk.END)
        self.job_title_entry.delete(0, tk.END)
        self.basic_salary_entry.delete(0, tk.END)
        self.age_entry.delete(0, tk.END)
        self.date_of_birth_entry.delete(0, tk.END)
        self.passport_details_entry.delete(0, tk.END)
        self.passport_details_entry.delete(0, tk.END)
        self.manager_id_entry.delete(0, tk.END)



    def show_add_client(self):
        self.clear_frame()
        tk.Label(self.frame, text="Add Client").grid(row=0, column=0, columnspan=2, pady=10)

        tk.Label(self.frame, text="Client ID:").grid(row=1, column=0)
        self.client_id_entry = tk.Entry(self.frame)
        self.client_id_entry.grid(row=1, column=1)

        tk.Label(self.frame, text="Name:").grid(row=2, column=0)
        self.name_entry = tk.Entry(self.frame)
        self.name_entry.grid(row=2, column=1)

        tk.Label(self.frame, text="Address:").grid(row=3, column=0)
        self.address_entry = tk.Entry(self.frame)
        self.address_entry.grid(row=3, column=1)

        tk.Label(self.frame, text="Contact:").grid(row=4, column=0)
        self.contact_entry = tk.Entry(self.frame)
        self.contact_entry.grid(row=4, column=1)

        tk.Label(self.frame, text="Budget:").grid(row=5, column=0)
        self.budget_entry = tk.Entry(self.frame)
        self.budget_entry.grid(row=5, column=1)

        add_button = tk.Button(self.frame, text="Add", command=self.add_client)
        add_button.grid(row=6, column=0, columnspan=2, pady=10)

    def show_delete_client(self):
        self.clear_frame()
        tk.Label(self.frame, text="Delete Client").grid(row=0, column=0, columnspan=2, pady=10)

        tk.Label(self.frame, text="Client ID:").grid(row=1, column=0)
        self.delete_client_id_entry = tk.Entry(self.frame)
        self.delete_client_id_entry.grid(row=1, column=1)

        delete_button = tk.Button(self.frame, text="Delete", command=self.delete_client)
        delete_button.grid(row=2, column=0, columnspan=2, pady=10)

    # Client Crud GUI
    def show_modify_client(self):
        self.clear_frame()
        tk.Label(self.frame, text="Modify Client").grid(row=0, column=0, columnspan=2, pady=10)

        tk.Label(self.frame, text="Client ID:").grid(row=1, column=0)
        self.modify_client_id_entry = tk.Entry(self.frame)
        self.modify_client_id_entry.grid(row=1, column=1)

        tk.Label(self.frame, text="New Name:").grid(row=2, column=0)
        self.new_name_entry = tk.Entry(self.frame)
        self.new_name_entry.grid(row=2, column=1)

        tk.Label(self.frame, text="New Address:").grid(row=3, column=0)
        self.new_address_entry = tk.Entry(self.frame)
        self.new_address_entry.grid(row=3, column=1)

        tk.Label(self.frame, text="New Contact:").grid(row=4, column=0)
        self.new_contact_entry = tk.Entry(self.frame)
        self.new_contact_entry.grid(row=4, column=1)

        tk.Label(self.frame, text="New Budget:").grid(row=5, column=0)
        self.new_budget_entry = tk.Entry(self.frame)
        self.new_budget_entry.grid(row=5, column=1)

        modify_button = tk.Button(self.frame, text="Modify", command=self.modify_client)
        modify_button.grid(row=6, column=0, columnspan=2, pady=10)

    def show_display_client(self):
        self.clear_frame()
        tk.Label(self.frame, text="Display Client Details").grid(row=0, column=0, columnspan=2, pady=10)

        tk.Label(self.frame, text="Client ID:").grid(row=1, column=0)
        self.display_client_id_entry = tk.Entry(self.frame)
        self.display_client_id_entry.grid(row=1, column=1)

        display_button = tk.Button(self.frame, text="Display", command=self.display_client)
        display_button.grid(row=2, column=0, columnspan=2, pady=10)

    def add_client(self):
        # Fetch values from entry fields
        client_id_str = self.client_id_entry.get().strip()
        name = self.name_entry.get().strip()
        address = self.address_entry.get().strip()
        contact = self.contact_entry.get().strip()
        budget_str = self.budget_entry.get().strip()

        # Perform validation
        if not all([client_id_str, name, address, contact, budget_str]):
            # If any required field is empty, show an error message
            messagebox.showerror("Error", "Please provide all required information.")
            return

        try:
            # Convert ID to integer
            client_id = int(client_id_str)

            if client_id <= 0:
                raise ValueError("Client ID must be a non-negative integer and zero.")

            # Convert budget to float
            budget = float(budget_str)

            if budget <= 0:
                raise ValueError("Budget must be a positive number.")

            # Create a Client object and add it to the system
            client = Client(client_id, name, address, contact, budget)
            # Add client to system
            self.system.add_client(client)
            messagebox.showinfo("Success", "Client added successfully!")
            # Clear entry fields after adding client
            self.clear_add_entry_fields_of_client()

        except ValueError as ve:
            # Handle specific validation errors
            messagebox.showerror("Error", str(ve))
        except Exception as e:
            # Handle other exceptions
            messagebox.showerror("Error", f"An error occurred: {str(e)}")

    def delete_client(self):
        # Fetch client ID from entry field
        client_id = self.delete_client_id_entry.get()

        # Delete client from the system
        self.system.delete_client(client_id)

        # Clear entry field after deleting client
        self.delete_client_id_entry.delete(0, tk.END)

    def modify_client(self):
        # Fetch client ID from entry field
        client_id = self.modify_client_id_entry.get().strip()
        # Fetch new details from entry fields
        new_name = self.new_name_entry.get().strip()
        new_address = self.new_address_entry.get().strip()
        new_contact = self.new_contact_entry.get().strip()
        new_budget_str = self.new_budget_entry.get().strip()

        if self.system.client_exists(client_id):
            # Perform validation
            if (new_name == "" or new_address == "" or new_contact == "" or new_budget_str == ""):
                # If any required field is empty, show an error message
                messagebox.showerror("Error", "Please provide all required information.")
                return

            try:
                # Convert budget to float
                new_budget = float(new_budget_str)

                if new_budget <= 0:
                    raise ValueError("Budget must be a positive number.")

                # Create a new Client object with updated details
                updated_client = Client(client_id, new_name, new_address, new_contact, new_budget)
                # Modify client details in the system
                self.system.modify_client(client_id, updated_client)
                # Clear entry fields after modifying client
                self.clear_update_entry_fields_of_client()

            except ValueError as ve:
                # Handle specific validation errors
                messagebox.showerror("Error", str(ve))
            except Exception as e:
                # Handle other exceptions
                messagebox.showerror("Error", f"An error occurred: {str(e)}")

        else:
            messagebox.showerror("Error", "Client not found with ID {}".format(client_id))

    def display_client(self):
        # Fetch client ID from entry field
        client_id = self.display_client_id_entry.get()

        # Fetch client details from the system
        client = self.system.display_client(client_id)

        # Display client details (or perform any action as required)
        if client:
            messagebox.showinfo("Client Details", f"Name: {client.name}\nAddress: {client.address}\n"
                                                    f"Contact: {client.contact}\nBudget: {client.budget}")
        else:
            messagebox.showerror("Error", f"Client not found with ID {client_id}")

        # Clear entry field after displaying client details
        self.display_client_id_entry.delete(0, tk.END)

    def clear_update_entry_fields_of_client(self):
        # Clear all entry fields after an operation
        self.modify_client_id_entry.delete(0, tk.END)
        self.new_name_entry.delete(0, tk.END)
        self.new_address_entry.delete(0, tk.END)
        self.new_contact_entry.delete(0, tk.END)
        self.new_budget_entry.delete(0, tk.END)

    def clear_add_entry_fields_of_client(self):
        # Clear all entry fields after an operation
        self.client_id_entry.delete(0, tk.END)
        self.name_entry.delete(0, tk.END)
        self.address_entry.delete(0, tk.END)
        self.contact_entry.delete(0, tk.END)
        self.budget_entry.delete(0, tk.END)

    # Guest Crud GUI
    def show_add_guest(self):
            self.clear_frame()
            tk.Label(self.frame, text="Add Guest").grid(row=0, column=0, columnspan=2, pady=10)

            tk.Label(self.frame, text="ID:").grid(row=1, column=0)
            self.id_entry = tk.Entry(self.frame)
            self.id_entry.grid(row=1, column=1)

            tk.Label(self.frame, text="Name:").grid(row=2, column=0)
            self.name_entry = tk.Entry(self.frame)
            self.name_entry.grid(row=2, column=1)

            tk.Label(self.frame, text="Address:").grid(row=3, column=0)
            self.address_entry = tk.Entry(self.frame)
            self.address_entry.grid(row=3, column=1)

            tk.Label(self.frame, text="Contact:").grid(row=4, column=0)
            self.contact_entry = tk.Entry(self.frame)
            self.contact_entry.grid(row=4, column=1)

            add_button = tk.Button(self.frame, text="Add", command=self.add_guest)
            add_button.grid(row=5, column=0, columnspan=2, pady=10)

    def show_delete_guest(self):
        self.clear_frame()
        tk.Label(self.frame, text="Delete Guest").grid(row=0, column=0, columnspan=2, pady=10)

        tk.Label(self.frame, text="Guest ID:").grid(row=1, column=0)
        self.delete_id_entry = tk.Entry(self.frame)
        self.delete_id_entry.grid(row=1, column=1)

        delete_button = tk.Button(self.frame, text="Delete", command=self.delete_guest)
        delete_button.grid(row=2, column=0, columnspan=2, pady=10)

    def show_modify_guest(self):
        self.clear_frame()
        tk.Label(self.frame, text="Modify Guest").grid(row=0, column=0, columnspan=2, pady=10)

        tk.Label(self.frame, text="Guest ID:").grid(row=1, column=0)
        self.modify_id_entry = tk.Entry(self.frame)
        self.modify_id_entry.grid(row=1, column=1)

        tk.Label(self.frame, text="New Name:").grid(row=2, column=0)
        self.new_name_entry = tk.Entry(self.frame)
        self.new_name_entry.grid(row=2, column=1)

        tk.Label(self.frame, text="New Address:").grid(row=3, column=0)
        self.new_address_entry = tk.Entry(self.frame)
        self.new_address_entry.grid(row=3, column=1)

        tk.Label(self.frame, text="New Contact:").grid(row=4, column=0)
        self.new_contact_entry = tk.Entry(self.frame)
        self.new_contact_entry.grid(row=4, column=1)

        modify_button = tk.Button(self.frame, text="Modify", command=self.modify_guest)
        modify_button.grid(row=5, column=0, columnspan=2, pady=10)

    def show_display_guest(self):
        self.clear_frame()
        tk.Label(self.frame, text="Display Guest Details").grid(row=0, column=0, columnspan=2, pady=10)

        tk.Label(self.frame, text="Guest ID:").grid(row=1, column=0)
        self.display_id_entry = tk.Entry(self.frame)
        self.display_id_entry.grid(row=1, column=1)

        display_button = tk.Button(self.frame, text="Display", command=self.display_guest)
        display_button.grid(row=2, column=0, columnspan=2, pady=10)

    def add_guest(self):
        # Fetch values from entry fields
        id_str = self.id_entry.get().strip()
        name = self.name_entry.get().strip()
        address = self.address_entry.get().strip()
        contact = self.contact_entry.get().strip()

        # Perform validation
        if not all([id_str, name, address, contact]):
            # If any required field is empty, show an error message
            messagebox.showerror("Error", "Please provide all required information.")
            return

        try:
            # Convert ID to integer
            guest_id = int(id_str)

            if guest_id <= 0:
                raise ValueError("Guest ID must be a non-negative integer and zero.")

            # Create a Guest object and add it to the system
            guest = Guest(guest_id, name, address, contact)
            # Add guest to system
            self.system.add_guest(guest)
            messagebox.showinfo("Success", "Guest added successfully!")
            # Clear entry fields after adding guest
            self.clear_add_entry_fields_of_guest()

        except ValueError as ve:
            # Handle specific validation errors
            messagebox.showerror("Error", str(ve))
        except Exception as e:
            # Handle other exceptions
            messagebox.showerror("Error", f"An error occurred: {str(e)}")

    def delete_guest(self):
        # Fetch guest ID from entry field
        guest_id = self.delete_id_entry.get()

        # Delete guest from the system
        self.system.delete_guest(guest_id)

        # Clear entry field after deleting guest
        self.delete_id_entry.delete(0, tk.END)

    def modify_guest(self):
        # Fetch guest ID from entry field
        guest_id = self.modify_id_entry.get().strip()
        # Fetch new details from entry fields
        new_name = self.new_name_entry.get().strip()
        new_address = self.new_address_entry.get().strip()
        new_contact = self.new_contact_entry.get().strip()

        if self.system.guest_exists(guest_id):
            # Perform validation
            if (new_name == "" or new_address == "" or new_contact == ""):
                # If any required field is empty, show an error message
                messagebox.showerror("Error", "Please provide all required information.")
                return

            try:
                # Create a new Guest object with updated details
                updated_guest = Guest(guest_id, new_name, new_address, new_contact)
                # Modify guest details in the system
                self.system.modify_guest(guest_id, updated_guest)
                # messagebox.showinfo("Success", "Guest details modified successfully!")
                # Clear entry fields after modifying guest
                self.clear_update_entry_fields_of_guest()

            except Exception as e:
                # Handle other exceptions
                messagebox.showerror("Error", f"An error occurred: {str(e)}")
        else:
            messagebox.showerror("Error", "Guest not found with ID {}".format(guest_id))

    def display_guest(self):
        # Fetch guest ID from entry field
        guest_id = self.display_id_entry.get()

        # Fetch guest details from the system
        guest = self.system.display_guest(guest_id)

        # Display guest details (or perform any action as required)
        if guest:
            messagebox.showinfo("Guest Details", f"Name: {guest.name}\nAddress: {guest.address}\n"
                                                  f"Contact: {guest.contact}")
        else:
            messagebox.showerror("Error", f"Guest not found with ID {guest_id}")

        # Clear entry field after displaying guest details
        self.display_id_entry.delete(0, tk.END)

    def clear_update_entry_fields_of_guest(self):
        # Clear all entry fields after an operation
        self.modify_id_entry.delete(0, tk.END)
        self.new_name_entry.delete(0, tk.END)
        self.new_address_entry.delete(0, tk.END)
        self.new_contact_entry.delete(0, tk.END)

    def clear_add_entry_fields_of_guest(self):
        # Clear all entry fields after an operation
        self.id_entry.delete(0, tk.END)
        self.name_entry.delete(0, tk.END)
        self.address_entry.delete(0, tk.END)
        self.contact_entry.delete(0, tk.END)

    # Supplier Crud GUI
    def show_add_supplier(self):
        self.clear_frame()
        tk.Label(self.frame, text="Add Supplier").grid(row=0, column=0, columnspan=2, pady=10)

        tk.Label(self.frame, text="Supplier ID:").grid(row=1, column=0)
        self.supplier_id_entry = tk.Entry(self.frame)
        self.supplier_id_entry.grid(row=1, column=1)

        tk.Label(self.frame, text="Name:").grid(row=2, column=0)
        self.name_entry = tk.Entry(self.frame)
        self.name_entry.grid(row=2, column=1)

        tk.Label(self.frame, text="Address:").grid(row=3, column=0)
        self.address_entry = tk.Entry(self.frame)
        self.address_entry.grid(row=3, column=1)

        tk.Label(self.frame, text="Contact:").grid(row=4, column=0)
        self.contact_entry = tk.Entry(self.frame)
        self.contact_entry.grid(row=4, column=1)

        tk.Label(self.frame, text="Supplier Type:").grid(row=5, column=0)
        self.supplier_type_entry = tk.Entry(self.frame)
        self.supplier_type_entry.grid(row=5, column=1)

        add_button = tk.Button(self.frame, text="Add", command=self.add_supplier)
        add_button.grid(row=6, column=0, columnspan=2, pady=10)

    def show_delete_supplier(self):
        self.clear_frame()
        tk.Label(self.frame, text="Delete Supplier").grid(row=0, column=0, columnspan=2, pady=10)

        tk.Label(self.frame, text="Supplier ID:").grid(row=1, column=0)
        self.delete_supplier_id_entry = tk.Entry(self.frame)
        self.delete_supplier_id_entry.grid(row=1, column=1)

        delete_button = tk.Button(self.frame, text="Delete", command=self.delete_supplier)
        delete_button.grid(row=2, column=0, columnspan=2, pady=10)

    def show_modify_supplier(self):
        self.clear_frame()
        tk.Label(self.frame, text="Modify Supplier").grid(row=0, column=0, columnspan=2, pady=10)

        tk.Label(self.frame, text="Supplier ID:").grid(row=1, column=0)
        self.modify_supplier_id_entry = tk.Entry(self.frame)
        self.modify_supplier_id_entry.grid(row=1, column=1)

        tk.Label(self.frame, text="New Name:").grid(row=2, column=0)
        self.new_name_entry = tk.Entry(self.frame)
        self.new_name_entry.grid(row=2, column=1)

        tk.Label(self.frame, text="New Address:").grid(row=3, column=0)
        self.new_address_entry = tk.Entry(self.frame)
        self.new_address_entry.grid(row=3, column=1)

        tk.Label(self.frame, text="New Contact:").grid(row=4, column=0)
        self.new_contact_entry = tk.Entry(self.frame)
        self.new_contact_entry.grid(row=4, column=1)

        tk.Label(self.frame, text="New Supplier Type:").grid(row=5, column=0)
        self.new_supplier_type_entry = tk.Entry(self.frame)
        self.new_supplier_type_entry.grid(row=5, column=1)

        modify_button = tk.Button(self.frame, text="Modify", command=self.modify_supplier)
        modify_button.grid(row=6, column=0, columnspan=2, pady=10)

    def show_display_supplier(self):
        self.clear_frame()
        tk.Label(self.frame, text="Display Supplier Details").grid(row=0, column=0, columnspan=2, pady=10)

        tk.Label(self.frame, text="Supplier ID:").grid(row=1, column=0)
        self.display_supplier_id_entry = tk.Entry(self.frame)
        self.display_supplier_id_entry.grid(row=1, column=1)

        display_button = tk.Button(self.frame, text="Display", command=self.display_supplier)
        display_button.grid(row=2, column=1, columnspan=2, pady=10)

    def add_supplier(self):
        supplier_id = self.supplier_id_entry.get().strip()
        name = self.name_entry.get().strip()
        address = self.address_entry.get().strip()
        contact = self.contact_entry.get().strip()
        supplier_type = self.supplier_type_entry.get().strip()

        if not all([supplier_id, name, address, contact, supplier_type]):
            messagebox.showerror("Error", "Please provide all required information.")
            return

        try:
            supplier_id = int(supplier_id)
            supplier = Supplier(supplier_id, name, address, contact, supplier_type)
            self.system.add_supplier(supplier)
            messagebox.showinfo("Success", "Supplier added successfully!")
            self.clear_add_entry_fields_of_supplier()
        except ValueError as ve:
            messagebox.showerror("Error", str(ve))
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {str(e)}")

    def delete_supplier(self):
        supplier_id = self.delete_supplier_id_entry.get().strip()
        if not supplier_id:
            messagebox.showerror("Error", "Please provide a supplier ID.")
            return

        try:
            supplier_id = int(supplier_id)
            self.system.delete_supplier(supplier_id)
            # messagebox.showinfo("Success", "Supplier deleted successfully!")
            self.delete_supplier_id_entry.delete(0, tk.END)
        except ValueError as ve:
            messagebox.showerror("Error", str(ve))
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {str(e)}")

    def modify_supplier(self):
        supplier_id = self.modify_supplier_id_entry.get().strip()
        new_name = self.new_name_entry.get().strip()
        new_address = self.new_address_entry.get().strip()
        new_contact = self.new_contact_entry.get().strip()
        new_supplier_type = self.new_supplier_type_entry.get().strip()

        if self.system.supplier_exists(supplier_id):
            if not all([supplier_id, new_name, new_address, new_contact, new_supplier_type]):
                messagebox.showerror("Error", "Please provide all required information.")
                return

            try:
                supplier_id = int(supplier_id)
                supplier = Supplier(supplier_id, new_name, new_address, new_contact, new_supplier_type)
                self.system.modify_supplier(supplier_id, supplier)
                # messagebox.showinfo("Success", "Supplier details modified successfully!")
                self.clear_modify_entry_fields_of_supplier()
            except ValueError as ve:
                messagebox.showerror("Error", str(ve))
            except Exception as e:
                messagebox.showerror("Error", f"An error occurred: {str(e)}")
        else:
            messagebox.showerror("Error", "Guest not found with ID {}".format(supplier_id))

    def display_supplier(self):
        supplier_id = self.display_supplier_id_entry.get().strip()
        if not supplier_id:
            messagebox.showerror("Error", "Please provide a supplier ID.")
            return

        try:
            supplier_id = int(supplier_id)
            supplier = self.system.display_supplier(supplier_id)
            if supplier:
                messagebox.showinfo("Supplier Details", f"Name: {supplier.name}\nAddress: {supplier.address}\n"
                                                         f"Contact: {supplier.contact}\nSupplier Type: {supplier.supplier_type}")
            else:
                messagebox.showerror("Error", f"Supplier not found with ID {supplier_id}")
            self.display_supplier_id_entry.delete(0, tk.END)
        except ValueError as ve:
            messagebox.showerror("Error", str(ve))
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {str(e)}")

    def clear_add_entry_fields_of_supplier(self):
        self.supplier_id_entry.delete(0, tk.END)
        self.name_entry.delete(0, tk.END)
        self.address_entry.delete(0, tk.END)
        self.contact_entry.delete(0, tk.END)
        self.supplier_type_entry.delete(0, tk.END)

    def clear_modify_entry_fields_of_supplier(self):
        self.modify_supplier_id_entry.delete(0, tk.END)
        self.new_name_entry.delete(0, tk.END)
        self.new_address_entry.delete(0, tk.END)
        self.new_contact_entry.delete(0, tk.END)
        self.new_supplier_type_entry.delete(0, tk.END)

    
    # Events - CRUD UI
    def show_add_event(self):
        self.clear_frame()
        tk.Label(self.frame, text="Add Event").grid(row=0, column=0, columnspan=2, pady=10)

        # Add labels and entry fields for event details
        tk.Label(self.frame, text="Event ID:").grid(row=1, column=0)
        self.event_id_entry = tk.Entry(self.frame)
        self.event_id_entry.grid(row=1, column=1)

        tk.Label(self.frame, text="Event Type:").grid(row=2, column=0)
        self.event_type_entry = tk.Entry(self.frame)
        self.event_type_entry.grid(row=2, column=1)

        tk.Label(self.frame, text="Theme:").grid(row=3, column=0)
        self.theme_entry = tk.Entry(self.frame)
        self.theme_entry.grid(row=3, column=1)

        tk.Label(self.frame, text="Date:").grid(row=4, column=0)
        self.date_entry = tk.Entry(self.frame)
        self.date_entry.grid(row=4, column=1)

        tk.Label(self.frame, text="Time:").grid(row=5, column=0)
        self.time_entry = tk.Entry(self.frame)
        self.time_entry.grid(row=5, column=1)

        tk.Label(self.frame, text="Duration:").grid(row=6, column=0)
        self.duration_entry = tk.Entry(self.frame)
        self.duration_entry.grid(row=6, column=1)

        tk.Label(self.frame, text="Venue Address:").grid(row=7, column=0)
        self.venue_address_entry = tk.Entry(self.frame)
        self.venue_address_entry.grid(row=7, column=1)

        tk.Label(self.frame, text="Client ID:").grid(row=8, column=0)
        self.client_id_entry = tk.Entry(self.frame)
        self.client_id_entry.grid(row=8, column=1)

        tk.Label(self.frame, text="Guest List:").grid(row=9, column=0)
        self.guest_list_entry = tk.Entry(self.frame)
        self.guest_list_entry.grid(row=9, column=1)

        tk.Label(self.frame, text="Catering Company:").grid(row=10, column=0)
        self.catering_company_entry = tk.Entry(self.frame)
        self.catering_company_entry.grid(row=10, column=1)

        tk.Label(self.frame, text="Cleaning Company:").grid(row=11, column=0)
        self.cleaning_company_entry = tk.Entry(self.frame)
        self.cleaning_company_entry.grid(row=11, column=1)

        tk.Label(self.frame, text="Decorations Company:").grid(row=12, column=0)
        self.decorations_company_entry = tk.Entry(self.frame)
        self.decorations_company_entry.grid(row=12, column=1)

        tk.Label(self.frame, text="Entertainment Company:").grid(row=13, column=0)
        self.entertainment_company_entry = tk.Entry(self.frame)
        self.entertainment_company_entry.grid(row=13, column=1)

        tk.Label(self.frame, text="Furniture Company:").grid(row=14, column=0)
        self.furniture_company_entry = tk.Entry(self.frame)
        self.furniture_company_entry.grid(row=14, column=1)

        tk.Label(self.frame, text="Invoice:").grid(row=15, column=0)
        self.invoice_entry = tk.Entry(self.frame)
        self.invoice_entry.grid(row=15, column=1)

        add_button = tk.Button(self.frame, text="Add", command=self.add_event)
        add_button.grid(row=16, column=0, columnspan=2, pady=10)

    def show_delete_event(self):
        self.clear_frame()
        tk.Label(self.frame, text="Delete Event").grid(row=0, column=0, columnspan=2, pady=10)

        # Add labels and entry fields for deleting event
        tk.Label(self.frame, text="Event ID:").grid(row=1, column=0)
        self.delete_event_id_entry = tk.Entry(self.frame)
        self.delete_event_id_entry.grid(row=1, column=1)

        delete_button = tk.Button(self.frame, text="Delete", command=self.delete_event)
        delete_button.grid(row=2, column=0, columnspan=2, pady=10)

    def show_modify_event(self):
        self.clear_frame()
        tk.Label(self.frame, text="Modify Event").grid(row=0, column=0, columnspan=2, pady=10)


        # Add labels and entry fields for modifying event
        tk.Label(self.frame, text="Event ID:").grid(row=1, column=0)
        self.modify_event_id_entry = tk.Entry(self.frame)
        self.modify_event_id_entry.grid(row=1, column=1)

        tk.Label(self.frame, text="New Event Type:").grid(row=2, column=0)
        self.new_event_type_entry = tk.Entry(self.frame)
        self.new_event_type_entry.grid(row=2, column=1)

        tk.Label(self.frame, text="New Theme:").grid(row=3, column=0)
        self.new_theme_entry = tk.Entry(self.frame)
        self.new_theme_entry.grid(row=3, column=1)

        tk.Label(self.frame, text="New Date:").grid(row=4, column=0)
        self.new_date_entry = tk.Entry(self.frame)
        self.new_date_entry.grid(row=4, column=1)

        tk.Label(self.frame, text="New Time:").grid(row=5, column=0)
        self.new_time_entry = tk.Entry(self.frame)
        self.new_time_entry.grid(row=5, column=1)

        tk.Label(self.frame, text="New Duration:").grid(row=6, column=0)
        self.new_duration_entry = tk.Entry(self.frame)
        self.new_duration_entry.grid(row=6, column=1)

        tk.Label(self.frame, text="New Venue Address:").grid(row=7, column=0)
        self.new_venue_address_entry = tk.Entry(self.frame)
        self.new_venue_address_entry.grid(row=7, column=1)

        tk.Label(self.frame, text="New Client ID:").grid(row=8, column=0)
        self.new_client_id_entry = tk.Entry(self.frame)
        self.new_client_id_entry.grid(row=8, column=1)

        tk.Label(self.frame, text="New Guest List:").grid(row=9, column=0)
        self.new_guest_list_entry = tk.Entry(self.frame)
        self.new_guest_list_entry.grid(row=9, column=1)

        tk.Label(self.frame, text="New Catering Company:").grid(row=10, column=0)
        self.new_catering_company_entry = tk.Entry(self.frame)
        self.new_catering_company_entry.grid(row=10, column=1)

        tk.Label(self.frame, text="New Cleaning Company:").grid(row=11, column=0)
        self.new_cleaning_company_entry = tk.Entry(self.frame)
        self.new_cleaning_company_entry.grid(row=11, column=1)

        tk.Label(self.frame, text="New Decorations Company:").grid(row=12, column=0)
        self.new_decorations_company_entry = tk.Entry(self.frame)
        self.new_decorations_company_entry.grid(row=12, column=1)

        tk.Label(self.frame, text="New Entertainment Company:").grid(row=13, column=0)
        self.new_entertainment_company_entry = tk.Entry(self.frame)
        self.new_entertainment_company_entry.grid(row=13, column=1)

        tk.Label(self.frame, text="New Furniture Company:").grid(row=14, column=0)
        self.new_furniture_company_entry = tk.Entry(self.frame)
        self.new_furniture_company_entry.grid(row=14, column=1)

        tk.Label(self.frame, text="New Invoice:").grid(row=15, column=0)
        self.new_invoice_entry = tk.Entry(self.frame)
        self.new_invoice_entry.grid(row=15, column=1)

        modify_button = tk.Button(self.frame, text="Modify", command=self.modify_event)
        modify_button.grid(row=16, column=1, columnspan=2, pady=10)

    def show_display_event(self):
        self.clear_frame()
        tk.Label(self.frame, text="Display Event Details").grid(row=0, column=0, columnspan=2, pady=10)

        # Add labels and entry fields for displaying event details
        tk.Label(self.frame, text="Event ID:").grid(row=1, column=0)
        self.display_event_id_entry = tk.Entry(self.frame)
        self.display_event_id_entry.grid(row=1, column=1)

        display_button = tk.Button(self.frame, text="Display", command=self.display_event)
        display_button.grid(row=2, column=0, columnspan=2, pady=10)

    def add_event(self):
        # Fetch values from entry fields
        event_id = self.event_id_entry.get().strip()
        event_type = self.event_type_entry.get().strip()
        theme = self.theme_entry.get().strip()
        date = self.date_entry.get().strip()
        time = self.time_entry.get().strip()
        duration = self.duration_entry.get().strip()
        venue_address = self.venue_address_entry.get().strip()
        client_id = self.client_id_entry.get().strip()
        guest_list = self.guest_list_entry.get().strip()
        catering_company = self.catering_company_entry.get().strip()
        cleaning_company = self.cleaning_company_entry.get().strip()
        decorations_company = self.decorations_company_entry.get().strip()
        entertainment_company = self.entertainment_company_entry.get().strip()
        furniture_company = self.furniture_company_entry.get().strip()
        invoice = self.invoice_entry.get().strip()

        # Perform validation
        if not all([event_id, event_type, theme, date, time, duration, venue_address, client_id, guest_list]):
            # If any required field is empty, show an error message
            messagebox.showerror("Error", "Please provide all required information.")
            return

        try:
            # Convert event_id to integer
            event_id = int(event_id)

            if event_id <= 0:
                raise ValueError("Event ID must be a non-negative integer and zero.")

            # Convert duration to integer
            duration = int(duration)

            if duration <= 0:
                raise ValueError("Duration must be a positive number.")

            # Create an Event object and add it to the system
            event = Event(event_id, event_type, theme, date, time, duration, venue_address, client_id, guest_list,
                        catering_company, cleaning_company, decorations_company, entertainment_company, furniture_company, invoice)
            # Add event to system
            self.system.add_event(event)
            messagebox.showinfo("Success", "Event added successfully!")
            # Clear entry fields after adding event
            self.clear_add_entry_fields_of_events()

        except ValueError as ve:
            # Handle specific validation errors
            messagebox.showerror("Error", str(ve))
        except Exception as e:
            # Handle other exceptions
            messagebox.showerror("Error", f"An error occurred: {str(e)}")

    def delete_event(self):
        # Fetch event ID from entry field
        event_id = self.delete_event_id_entry.get().strip()

        # Delete event from the system
        self.system.delete_event(event_id)
        # messagebox.showinfo("Success", "Event deleted successfully!")

        # Clear entry field after deleting event
        self.delete_event_id_entry.delete(0, tk.END)


    def modify_event(self):
        # Fetch event ID from entry field
        event_id = self.modify_event_id_entry.get().strip()

        if self.system.event_exists(event_id):
            # Fetch new details from entry fields
            new_event_type = self.new_event_type_entry.get().strip()
            new_theme = self.new_theme_entry.get().strip()
            new_date = self.new_date_entry.get().strip()
            new_time = self.new_time_entry.get().strip()
            new_duration = self.new_duration_entry.get().strip()
            new_venue_address = self.new_venue_address_entry.get().strip()
            new_client_id = self.new_client_id_entry.get().strip()
            new_guest_list = self.new_guest_list_entry.get().strip()
            new_catering_company = self.new_catering_company_entry.get().strip()
            new_cleaning_company = self.new_cleaning_company_entry.get().strip()
            new_decorations_company = self.new_decorations_company_entry.get().strip()
            new_entertainment_company = self.new_entertainment_company_entry.get().strip()
            new_furniture_company = self.new_furniture_company_entry.get().strip()
            new_invoice = self.new_invoice_entry.get().strip()

            try:
                # Perform validation
                if not all([new_event_type, new_theme, new_date, new_time, new_duration, new_venue_address,new_client_id, new_guest_list]):
                    raise ValueError("Please provide all required information.")

                # Convert new_duration to integer
                new_duration = int(new_duration)

                if new_duration <= 0:
                    raise ValueError("Duration must be a positive number.")

                # Create a new Event object with updated details
                updated_event = Event(event_id, new_event_type, new_theme, new_date, new_time, new_duration, new_venue_address,
                                    new_client_id, new_guest_list, new_catering_company, new_cleaning_company,
                                    new_decorations_company, new_entertainment_company, new_furniture_company, new_invoice)
                # Modify event details in the system
                self.system.modify_event(event_id, updated_event)
                # messagebox.showinfo("Success", "Event details modified successfully!")
                # Clear entry fields after modifying event
                self.clear_modify_entry_fields_of_events()

            except Exception as e:
                # Handle any errors that occur during modification
                print(str(e))
                messagebox.showerror("Error", f"An error occurred: {str(e)}")

        else:
            messagebox.showerror("Error", f"Event not found with ID {event_id}")

    def display_event(self):
        # Fetch event ID from entry field
        event_id = self.display_event_id_entry.get().strip()

        try:
            # Perform validation
            if not event_id:
                raise ValueError("Please provide the event ID.")

            # Convert event_id to integer
            event_id = int(event_id)

            if event_id <= 0:
                raise ValueError("Event ID must be a non-negative integer and zero.")

            # Fetch event details from the system
            event = self.system.display_event(event_id)

            # Display event details (or perform any action as required)
            if event:
                details = (
                    f"Event ID: {event.event_id}\n"
                    f"Event Type: {event.event_type}\n"
                    f"Theme: {event.theme}\n"
                    f"Date: {event.date}\n"
                    f"Time: {event.time}\n"
                    f"Duration: {event.duration}\n"
                    f"Venue Address: {event.venue_address}\n"
                    f"Client ID: {event.client_id}\n"
                    f"Guest List: {event.guest_list}\n"
                    f"Catering Company: {event.catering_company}\n"
                    f"Cleaning Company: {event.cleaning_company}\n"
                    f"Decorations Company: {event.decorations_company}\n"
                    f"Entertainment Company: {event.entertainment_company}\n"
                    f"Furniture Company: {event.furniture_company}\n"
                    f"Invoice: {event.invoice}"
                )
                messagebox.showinfo("Event Details", details)
            else:
                messagebox.showerror("Error", f"Event not found with ID {event_id}")

        except ValueError as ve:
            # Handle specific validation errors
            messagebox.showerror("Error", str(ve))
        except Exception as e:
            # Handle other exceptions
            messagebox.showerror("Error", f"An error occurred: {str(e)}")

        # Clear entry field after displaying event details
        self.display_event_id_entry.delete(0, tk.END)


    def clear_modify_entry_fields_of_events(self):
        # Clear all entry fields related to modifying an event
        self.modify_event_id_entry.delete(0, tk.END)
        self.new_event_type_entry.delete(0, tk.END)
        self.new_theme_entry.delete(0, tk.END)
        self.new_date_entry.delete(0, tk.END)
        self.new_time_entry.delete(0, tk.END)
        self.new_duration_entry.delete(0, tk.END)
        self.new_venue_address_entry.delete(0, tk.END)
        self.new_client_id_entry.delete(0, tk.END)
        self.new_guest_list_entry.delete(0, tk.END)
        self.new_catering_company_entry.delete(0, tk.END)
        self.new_cleaning_company_entry.delete(0, tk.END)
        self.new_decorations_company_entry.delete(0, tk.END)
        self.new_entertainment_company_entry.delete(0, tk.END)
        self.new_furniture_company_entry.delete(0, tk.END)
        self.new_invoice_entry.delete(0, tk.END)


    def clear_add_entry_fields_of_events(self):
        # Clear all entry fields after an operation
        self.event_id_entry.delete(0, tk.END)
        self.event_type_entry.delete(0, tk.END)
        self.theme_entry.delete(0, tk.END)
        self.date_entry.delete(0, tk.END)
        self.time_entry.delete(0, tk.END)
        self.duration_entry.delete(0, tk.END)
        self.venue_address_entry.delete(0, tk.END)
        self.client_id_entry.delete(0, tk.END)
        self.guest_list_entry.delete(0, tk.END)
        self.catering_company_entry.delete(0, tk.END)
        self.cleaning_company_entry.delete(0, tk.END)
        self.decorations_company_entry.delete(0, tk.END)
        self.entertainment_company_entry.delete(0, tk.END)
        self.furniture_company_entry.delete(0, tk.END)
        self.invoice_entry.delete(0, tk.END)
        
if __name__ == "__main__":
    system = EventManagementSystem()
    app = MainApplication(system)
    app.mainloop()
