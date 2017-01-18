import abc, random, datetime

class Institution(abc.ABCMeta('ABC', (object,), {})):
	registration_date = datetime.date.today()
	
	def get_registration_date(self):
		return self.registration_date
	
	@abc.abstractmethod
	def mission(self):
		pass

class Department(object):
	
	def __init__(self, name):
		self.name = name
	
	@classmethod
	def generate_job_id(self, cls):
		return random.randint(1000, 5000)

class Employee(Institution, Department):
	
	def __init__(self, name, dept):
		self.name = name
		self.department = Department(dept)
		self.id = Department.generate_job_id(self.department)
		
	def mission(self):
		return 'I, ' + self.name + ' - ' + str(self.id) + ', want to be amongst the top world class developers'
		
emp = Employee('Nathan', 'IT')
print emp.mission()
print 'I was registered on ' + unicode(emp.get_registration_date())
