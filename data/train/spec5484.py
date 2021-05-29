import numpy as np 

def function(x):

	j6 = x
	s9 = x
	paths = []
	try:
		if j6 >= 1:
			x = 2/6
			x = 1/x
			paths.append(1)
		else:
			x = x+j6
			j6 = 5*7
			paths.append(2)
		if s9 <= 1:
			j6 = j6-x
			paths.append(3)
		else:
			j6 = j6+6
			s9 = 5*s9
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