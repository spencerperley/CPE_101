class Empl:
    
    employees = [] #Class variable for storing all employees
    
    def __init__(self, name, age, position=None):
        '''Constructor that assignees each of the attributes and adds the objects to a list'''

        self.name = name
        self.age = int(age)
        self.position = position

        Empl.employees.append(self)

    def __str__(self):
        '''Standard __str__ method to print cleanly'''
        return (self.name + ", " + str(self.age) + ", " + self.position)
    
    def __repr__(self):
        '''Simple representation method'''
        return(self.name,self.age,self.position)

    def displayEmployees():
        '''A static method that takes all of the instantiated employees
        and prints them out'''

        print("Employees in Dunder Mifflin are:")
        for employee in Empl.employees:
            print(employee)
            
    def allocateDepartment(departmentNames, emplList): 
        #department names list should be formated as a list of tuples (department keyword, department name)
        '''This static method takes 2 lists. The first is the department names and the second is the list of employees.
        Then for each apartment name each employee is checked to see if the department key name is in the employee description.
        then a list of tuples is returned formated like this [(department name,[employee1,employee2...])...'''
        
        departments = []
        for departmentName in departmentNames:
            tempTuple = (departmentName[1],[])
            departments.append(tempTuple)
            for empl in emplList:
                if str(departmentName[0]).lower() in  str(empl.position).lower(): #lower included so it is not case sensitive
                    departments[len(departments)-1][1].append(empl)
        return (departments)
    
    def headOfDepartment(departments):
        '''This static method sorts the list of departments by age and then the employee with the highest age has "Head " added to their position '''
        
        for i in range(0,len(departments)):
            sortedDepartments = sorted(departments[i][1],key = lambda employee : employee.age, reverse=True)
            '''Anonymous function to sort by specifically age. Not sure if I have to comment on this but better safe than sorry'''
            departments[i][1].clear()
            for j in range(0,len(sortedDepartments)): 
                departments[i][1].append(sortedDepartments[j])
            departments[i][1][0].position = "Head " + departments[i][1][0].position
    
    def displayDepartmentEmployees(departments):
        '''Iterates through the departments list and prints it'''
        
        for department in departments:
            print(" \n" +department[0] + ":")
            for employee in department[1]:
                print(employee)
    

people = [["Michael", 45, "Manager"],
          ["Dwight", 40, "Assistant to the Manager"],
          ["Jim", 35, "Manager"],
          ["Pam", 30, "Receptionist"],
          ["Angela", 32, "Accountant"],
          ["Kevin", 42, "Accountant"],
          ["Oscar", 40, "Accountant"],
          ["Stanley", 55, "Salesperson"],
          ["Phyllis", 45, "Salesperson"],
          ["Andy", 38, "Salesperson"],
          ["Ryan", 30, "Salesperson"],
          ["Creed", 55, "Salesperson"]]

departmentNames = [("Manager","Management"),("Accountant","Accounts"),("Salesperson","Sales")]


for i in people:
    Empl(i[0], i[1], i[2])
    
'''All of the methods being called and printed'''
print(" \n-- This is all of the employees --\n ")
Empl.displayEmployees()

print(" \n-- This is the initial department list --")
departmentsList = Empl.allocateDepartment(departmentNames,Empl.employees)
Empl.displayDepartmentEmployees(departmentsList)

print(" \n-- This is the department list which includes the department heads --")
Empl.headOfDepartment(departmentsList)
Empl.displayDepartmentEmployees(departmentsList)