import numpy as np 

def function(x):

	s9 = 6
	u6 = 5
	paths = []
	try:
		if s9 > 3:
			u6 = 5*x
			x = 5-x
			x = 8-x
			paths.append(1)
		else:
			u6 = u6-s9
			s9 = 4-s9
			paths.append(2)
		if u6 >= 9:
			s9 = 4/s9
			x = 2*x
			paths.append(3)
		else:
			s9 = s9/u6
			s9 = s9*s9
			paths.append(4)
		paths.append(5)
		assert x >= 0
		x = x**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))