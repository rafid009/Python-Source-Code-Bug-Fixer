import numpy as np 

def function(x):

	a0 = 9
	s4 = 7
	paths = []
	try:
		if s4 <= 9:
			a0 = a0-x
			paths.append(1)
		else:
			x = x-2
			a0 = s4+6
			paths.append(2)
		if s4 < 1:
			s4 = s4/8
			paths.append(3)
		else:
			a0 = s4-8
			paths.append(4)
		paths.append(5)
		assert x >= 0
		a0 = x**0.5
		return a0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))