"""
# Definition for Employee.
class Employee:
    def __init__(self, id: int, importance: int, subordinates: List[int]):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates
"""

class Solution:
    def getImportance(self, employees: List['Employee'], id: int) -> int:
        emp = None
        s = 0
        q= []
        q.append(self.findId(employees,id))
        while len(q):
            e = q.pop()
            s += e.importance
            for i in e.subordinates:
                q.append(self.findId(employees,i))
        
        return s
        
    def findId(self,emp,id):
        for i in range(len(emp)):
            employee = emp[i]
            if employee.id == id:
                return employee
