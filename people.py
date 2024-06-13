from typing import Optional
"""
We'll try to understand classes in python. 
Check the resources on google classroom to ensure you have gone through everything expected.

"""
###### THESE LISTS HAVE ALREADY BEEN DEFINED FOR YOU ###############
engineer_roster = [] # A list of all instantiated engineer objects
sales_roster = [] # List of all instantiated sales objects
branchmap = {  # A dictionary of dictionaries -> Maps branchcodes to cities and branch names
    0:  { "city": "NYC", "name": "Hudson Yards"},
    1:  { "city": "NYC" , "name": "Silicon Alley"},
    2:  { "city": "Mumbai", "name": "BKC"},
    3:  { "city": "Tokyo", "name": "Shibuya"},
    4:  { "city": "Mumbai", "name": "Goregaon"},
    5:  { "city": "Mumbai", "name": "Fort"}
}
####################################################################

class Employee:
    name : str 
    age : int
    ID : int
    city : int
    branches : list[int] # This is a list of branches (as branch codes) to which the employee may report
    salary : int 

    def __init__(self, name, age, ID, city,\
                 branchcodes, salary = None):
        self.name = name
        self.age = age 
        self.ID = ID
        self.city = city
        self.branches = branchcodes
        if salary is not None: self.salary = salary
        else: self.salary = 10_000 
        
    
    def change_city(self, new_city:str) -> bool:
        if self.city != new_city:
            self.city = new_city
            return True
        else:
            return False
        # Change the city 
        # Return true if city change, successful, return false if city same as old city
       

    def migrate_branch(self, new_code:int) -> bool:
        if len(self.branches)!=1:
            return False
        else :
            current_branch_code = self.branches[0]
            if branchmap[current_branch_code]['city'] == branchmap[new_code]['city']:
                self.branches[0] = new_code
                return True
            else:
                return False
        # Should work only on those employees who have a single 
        # branch to report to. Fail for others.
        # Change old branch to new if it is in the same city, else return false.
        

    def increment(self, increment_amt: int) -> None:
        # Increment salary by amount specified.
        self.salary+=increment_amt
        





class Engineer(Employee):
    position : str # Position in organization Hierarchy

    def __init__(self, name, age, ID, city,\
                 branchcodes, position= "Junior", salary = None):
        # Call the parent's constructor  
        super().__init__(name, age, ID, city, branchcodes, salary)
        positions_allowed=["Junior","Senior", "Team Lead", "Director" ]
        t=0
        for pos in positions_allowed:
            if(position==pos): 
             self.position=position
             t=1
             break
        if(t==0):
         raise ValueError(f"Invalid position: {position}")
        else: 
         self.t=t
        # Check if position is one of  "Junior", "Senior", "Team Lead", or "Director" 
        # Only then set the position. 
         engineer_roster.append(self)
        
    
    def increment(self, amt:int) -> None:
        self.salary+=(amt*1.1)
        # While other functions are the same for and engineer,
        # and increment to an engineer's salary should add a 10% bonus on to "amt"
        pass
        
    def promote(self, position:str) -> bool:
        positions_allowed=["Junior","Senior", "Team Lead", "Director" ]
        if position not in positions_allowed:
            return False
        current_index = positions_allowed.index(self.position)
        new_index = positions_allowed.index(position)
        if new_index <= current_index:
            return False
        self.increment(self.salary*0.3)
        self.position = position
        return True
        # Return false for a demotion or an invalid promotion
        # Promotion can only be to a higher position and
        # it should call the increment function with 30% of the present salary
        # as "amt". Thereafter return True.
        pass



class Salesman(Employee):
    """ 
    This class is to be entirely designed by you.

    Add increment (this time only a 5% bonus) and a promotion function
    This time the positions are: Rep -> Manager -> Head.

    Add an argument in init which tracks who is the superior
    that the employee reports to. This argument should be the ID of the superior
    It should be None for a "Head" and so, the argument should be optional in init.
    """ 
    
    # An extra member variable!
    superior : int # EMPLOYEE ID of the superior this guy reports to
    superior_id:  Optional[int]
    def __init__(self, name, age, ID, city,\
                 branchcodes, position= "Rep", salary = None):
        # Call the parent's constructor  
        super().__init__(name, age, ID, city, branchcodes, salary)
        positions_allowed=["Rep","Manager", "Head"]
        t=0
        f=0
        for pos in positions_allowed:
            t+=1
            if(position==pos): 
             self.position=position
             f=1
             break
        if(t==0):
         raise ValueError(f"Invalid position: {position}")
        else: 
         self.t=t
         sales_roster.append(self)
        
            
    
    # def promote 
    def promote(self, position:str) -> bool:
        positions_allowed=["Rep","Manager", "Head"]
        if position not in positions_allowed:
            return False
        current_index = positions_allowed.index(self.position)
        new_index = positions_allowed.index(position)
        if new_index <= current_index:
            return False
        self.increment(self.salary*0.3)
        self.position = position
        return True
    # def increment 
    def increment(self, amt:int) -> None:
         self.salary+=(amt*1.05)
        





    def find_superior(self) -> tuple[int, str]:
        if(self.t==3):
            return(None,None)
        for salesman in sales_roster:
            if(salesman.t>self.t):
                return(salesman.ID,salesman.name)
            
        # Return the employee ID and name of the superior
        # Report a tuple of None, None if no superior.
        




    def add_superior(self) -> bool:
        if(self.t==3):
            return False
        for salesman in sales_roster:
            if(salesman.t>self.t):
                self.superior_id = salesman.ID
        # Add superior of immediately higher rank.
        # If superior doesn't exist return false,





    def migrate_branch(self, new_code: int) -> bool:
        # This should simply add a branch to the list; even different cities are fine
        if new_code not in self.branches:
            self.branches.append(new_code)
            return True
        return False
        pass

    





    
    