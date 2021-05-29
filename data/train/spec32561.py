import numpy as np 

def function(x):

	e4 = x
	s1 = x
	paths = []
	try:
		if s1 >= 2:
			s1 = 6+s1
			s1 = s1*s1
			x = x-8
			paths.append(1)
		else:
			x = x+3
			paths.append(2)
		if e4 >= 5:
			e4 = 5*e4
			paths.append(3)
		else:
			x = 8/x
			paths.append(4)
		paths.append(5)
		assert s1 >= 0
		e4 = s1**0.5
		return e4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))