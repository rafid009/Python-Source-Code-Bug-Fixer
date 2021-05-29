import numpy as np 

def function(x):

	s1 = 7
	e1 = 5
	paths = []
	try:
		if e1 > 3:
			x = x/1
			s1 = 4*s1
			s1 = 7-s1
			paths.append(1)
		else:
			s1 = e1-9
			e1 = e1*s1
			s1 = s1+6
			paths.append(2)
		if s1 > 7:
			e1 = 0-x
			e1 = e1-6
			x = 7-x
			paths.append(3)
		else:
			x = 6/e1
			paths.append(4)
		paths.append(5)
		assert s1 >= 0
		e1 = s1**0.5
		return e1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))