"""
This is where the actual working of the program will happen!
We'll be Querying stuff for testing whether your classes were defined correctly

Whenever something inappropriate happens (like a function returning false in people.py),
raise a Value Error.
"""
from people import * # import everything!

if __name__ == "__main__":  # Equivalent to int main() {} in C++.
    last_input = 99
    while last_input != 0:
        last_input = int(input("Please enter a query number:"))

        if last_input == 1:
            name = input("Name:")
            ID = input("ID:")
            city = input("City:")
            branchcodes = input("Branch(es):")
            branchcodes = [int(code.strip()) for code in branchcodes.split(',')]
            # How will you convert this to a list, given that
            # the user will always enter a comma separated list of branch codes?
            # eg>   2,5

            salary = input("Salary: ")
            age=input("age:")
            position=input("positon is:")
            # Create a new Engineer with given details.
            engineer = Engineer(name, age,ID,city,branchcodes,position,salary) # Change this

            engineer_roster.append(engineer) # Add him to the list! See people.py for definiton
            
        


        elif last_input == 2:
         


            name = input("Name:")
            ID = input("ID:")
            city = input("City:")
            branchcodes = input("Branch(es):")
            branchcodes = [int(code.strip()) for code in branchcodes.split(',')]

            salary = input("Salary: ")
            age=input("age:")
            position=input("positon is:")    


            salesman = Salesman(name, age,ID,city,branchcodes,position,salary)
            sales_roster.append(salesman)




            # Gather input to create a Salesperson
            # Then add them to the roster
            

        elif last_input == 3:
            ID = int(input("ID: "))
            # Print employee details for the given employee ID that is given. 
            
            found_employee = None
            for employee in engineer_roster + sales_roster:
                if employee.ID == int(ID):
                    found_employee = employee
                    break
            
            if not found_employee: print("No such employee")
            else:
                print(f"Name: {found_employee.name} and Age: {found_employee.age}")
                print(f"City of Work: {found_employee.city}")

                ## Write code here to list the branch names to
                ## which the employee reports as a comma separated list
                ## eg> Branches: Goregaon,Fort
                branch_names = [branchmap[code]['name'] for code in found_employee.branches]

                ## ???? what comes here??
                # print(f"Branches: " + ???? )
                print(f"Branches: {', '.join(branch_names)}")
                print(f"Salary: {found_employee.salary}")

        elif last_input == 4:
            #### NO IF ELSE ZONE ######################################################
            # Change branch to new branch or add a new branch depending on class
            # Inheritance should automatically do this. 
            # There should be no IF-ELSE or ternary operators in this zone
            ID = int(input("Enter Employee ID to promote: "))
             
            pass
            #### NO IF ELSE ZONE ENDS #################################################

        elif last_input == 5:
            ID = int(input("Enter Employee ID to promote: "))
            position=input("promote to:")
            for employee in engineer_roster + sales_roster:
                if employee.ID == ID:
                    employee.promote(position)
            # promote employee to next position

        elif last_input == 6:
            ID = int(input("Enter Employee I  D to give increment: "))
            increment_amt=int(input("increment should be"))
            for employee in engineer_roster + sales_roster:
                if employee.ID == ID:
                    employee.increment(increment_amt)
            # Increment salary of employee.
        
        elif last_input == 7:
            ID = int(input("Enter Employee ID to find superior: "))
            for employee in sales_roster:
                if employee.ID == ID:
                    employee.find_superior()

            # Print superior of the sales employee.
        
        elif last_input == 8:
            ID = int(input("Enter Employee ID to add superior: "))
           
            for employee in sales_roster:
                if employee.ID == ID:
                     employee.add_superior()

            # Add superior of a sales employee

        else:
            raise ValueError("No such query number defined")

            
            

            


            


        






