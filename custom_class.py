from abc import ABC
import random

class Institution(object):
	name = "Andela Co"
	def __init__(self):
		self.registration_date = 
	
	def get_registration_date(self):
		return self.registration_date = 
	
	@abc.abstractmethod
	def mission(self):
		pass

class Department(object):
	employees = []
	
	def __init__(self, name, organisation):
		self.name = name
	
	def add_employee(self, employee_id):
		employees.append(employee_id)
		return self
		
	def remove_employee(self, employee_id):
		employees.pop(employees.index(employee_id));
		return self
		
	def generate_job_id(self):
		return random.randint(1000, 5000, 2)
		
class Employee(object, Institution, Department):
	
	def __init__(self, name, job_id):
		self.name = name
		self.job_id = generate_job_id()
		add_employee(self.job_id)
		
	def mission(self):
		return self.name + ' want to be amongst the top world class developers'
