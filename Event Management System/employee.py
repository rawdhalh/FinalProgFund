class Employee:
    def __init__(self, id, name, department, job_title, basic_salary, age, date_of_birth, passport_details, manager_id):
        self.id = id
        self.name = name
        self.department = department
        self.job_title = job_title
        self.basic_salary = basic_salary
        self.age = age
        self.date_of_birth = date_of_birth
        self.passport_details = passport_details
        self.manager_id = manager_id
    
    def __str__(self):
        return f"Employee ID: {self.id}\nName: {self.name}\nDepartment: {self.department}\nJob Title: {self.job_title}\nBasic Salary: {self.basic_salary}\nAge: {self.age}\nDate of Birth: {self.date_of_birth}\nPassport Details: {self.passport_details}\nManager ID: {self.manager_id}"