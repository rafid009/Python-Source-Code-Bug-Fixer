import numpy as np 

def function(x):

	o1 = x
	s9 = x
	paths = []
	try:
		if x < 5:
			s9 = s9+o1
			paths.append(1)
		else:
			x = 9-x
			paths.append(2)
		if o1 >= 8:
			x = o1*x
			s9 = s9-4
			paths.append(3)
		else:
			x = x*x
			s9 = s9-6
			s9 = x/4
			paths.append(4)
		paths.append(5)
		assert x >= 0
		s9 = x**0.5
		return s9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))