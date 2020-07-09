Python 3.8.3 (tags/v3.8.3:6f8c832, May 13 2020, 22:20:19) [MSC v.1925 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> class Student:
	def __init__()		#constructor defining
	
SyntaxError: invalid syntax
>>> class Student:
	def __init__()		#constructor defining
	
SyntaxError: invalid syntax
>>> class Student:
	def __init__()		#constructor defining
	
SyntaxError: invalid syntax
>>> class Student:
	def __init__()
	
SyntaxError: invalid syntax
>>> class Student:
	def __init__(self,name,roll):
		self.name=name
		self.roll=roll

		
>>> class Student:
	def __init__(self,name,roll):
		self.name=name
		self.roll=roll
	def prints(self)
	
SyntaxError: invalid syntax
>>> class Student:
	def __init__(self,name,roll):
		self.name=name
		self.roll=roll
	def prints(self):
		print("name: ",self.name,"roll: ",self.roll)

		
>>> s1=Student("tharun",108)
>>> s1.prints()
name:  tharun roll:  108
>>> class Student:
	def __init__(self,name,roll):
		self.name=name
		self.roll=roll
	def prints(self):
		print("name: ",self.name,"\nroll: ",self.roll)

		
>>> s1=Student("tharun",108)
>>> s1.prints()
name:  tharun 
roll:  108
>>> s1.name
'tharun'
>>> s1.roll
108
>>> type(s1)
<class '__main__.Student'>
>>> names=["sat","rak","mur"]
>>> roll=[111,112,113]
>>> names=["sat","rak","sau"]
>>> students=[]
>>> type(students)
<class 'list'>
>>> for i in range(3):
	 students.append(Student(names[i],roll[i]))

	 
>>> students[0].prints()
name:  sat 
roll:  111
>>> students[2].prints()
name:  sau 
roll:  113
>>> for i in students
SyntaxError: invalid syntax
>>> for i in students:
	i.prints()

	
name:  sat 
roll:  111
name:  rak 
roll:  112
name:  sau 
roll:  113
>>> for i in students:
	i.prints()
	print("\n")

	
name:  sat 
roll:  111


name:  rak 
roll:  112


name:  sau 
roll:  113


>>> class Student:
	def __init__(self,**p):
		self.__dict__=p
	def prints(self):
		print(self.__dict__)

		
>>> students[0].__dict__
{'name': 'sat', 'roll': 111}
>>> del Student
>>> type(s1)
<class '__main__.Student'>
>>> class Student:
	def __init__(self,name,roll):
		self.name=name
		self.roll=roll
	def prints(self):
		print("name: ",self.name,"\nroll: ",self.roll)

		
>>> students[0].__dict__
{'name': 'sat', 'roll': 111}
>>> class Student:
	def __init__(self,name,roll):
		self.name=name
		self.roll=roll
	def prints(self):
		print("name: ",self.name,"roll: ",self.roll)

		
>>> students[0].__dict__
{'name': 'sat', 'roll': 111}
>>> students[0].prints()
name:  sat 
roll:  111
>>> stud=[]
>>> for i in range(3):
	 stud.append(Student(names[i],roll[i]))

	 
>>> stud[0].prints()
name:  sat roll:  111
>>> stud[0].__dict__
{'name': 'sat', 'roll': 111}
>>> class Employe:
	def __init__(self,**p):
		self.__dict__=p
	def prints(self):
		print(self.__dict__)

		
>>> emp=Employe(name="tharun",roll=108,cgpa=10.0)
>>> emp.prints()
{'name': 'tharun', 'roll': 108, 'cgpa': 10.0}
>>> emp.name
'tharun'
>>> emp.rank
Traceback (most recent call last):
  File "<pyshell#69>", line 1, in <module>
    emp.rank
AttributeError: 'Employe' object has no attribute 'rank'
>>> emp.roll
108
>>> emp2=Employe(name="rak",roll=112,rank=1)
>>> emp2.prints()
{'name': 'rak', 'roll': 112, 'rank': 1}

>>> emp2.rank
1
>>> emp2.cgpa
Traceback (most recent call last):
  File "<pyshell#74>", line 1, in <module>
    emp2.cgpa
AttributeError: 'Employe' object has no attribute 'cgpa'
>>> vars(emp)
{'name': 'tharun', 'roll': 108, 'cgpa': 10.0}
>>> vars(emp2)
{'name': 'rak', 'roll': 112, 'rank': 1}
>>> dir(emp)
['__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', 'cgpa', 'name', 'prints', 'roll']
>>> dir(emp2)
['__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', 'name', 'prints', 'rank', 'roll']
>>> getattr(emp,cgpa)
Traceback (most recent call last):
  File "<pyshell#79>", line 1, in <module>
    getattr(emp,cgpa)
NameError: name 'cgpa' is not defined
>>> getattr(s1,roll)
Traceback (most recent call last):
  File "<pyshell#80>", line 1, in <module>
    getattr(s1,roll)
TypeError: getattr(): attribute name must be string
>>> getattr(s1,"roll")
108
>>> getattr(emp,"cgpa")
10.0
>>> 
>>> def myobj(obj)
SyntaxError: invalid syntax
>>> def myobj(obj):
	obj.prints()

	
>>> myobj(s1)
name:  tharun 
roll:  108
>>> myobj(emp)
{'name': 'tharun', 'roll': 108, 'cgpa': 10.0}
>>> 