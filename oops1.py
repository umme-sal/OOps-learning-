class employee:
    def __init__(self):
        self.name = "Adi"
        self.id = 101
        self.dep = "IT"
        self.salary = 50000
        self.designation = "Software Engineer"
        self.age = 25

    def __init__(self, name, id,dep,salary,designation):
        self.name = name
        self.id = id
        self.dep = dep
        self.salary = salary
        self.designation = designation

    def display(self):
        print("Name:", self.name)
        print("ID:", self.id)
        print("Department:", self.dep)
        print("Salary:", self.salary)
        print("Designation:", self.designation)


ob1=employee("Adi", 101, "IT", 50000, "Software Engineer")
ob1.display()