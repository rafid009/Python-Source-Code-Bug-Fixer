import numpy as np 

def function(x):

	s4 = x
	s9 = 8
	paths = []
	try:
		if x <= 4:
			s4 = s9*s4
			paths.append(1)
		else:
			s4 = s4/5
			s9 = s9-3
			s9 = 2-0
			paths.append(2)
		if s9 > 8:
			x = x-8
			x = s4-x
			x = 9/4
			paths.append(3)
		else:
			s9 = 6-x
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