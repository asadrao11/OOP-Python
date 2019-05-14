class Employee:
    def __init__(self, fname, lname, salary):

        self.fname = fname
        self.lname = lname
        self.salary = salary

asad = Employee('asad', 'rao', 5500)
sarim = Employee('sarim', 'khan', 1500)

print(asad.fname, asad.lname, asad.salary)
print(sarim.fname, sarim.lname, sarim.salary)
    
