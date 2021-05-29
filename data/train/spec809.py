import numpy as np 

def function(x):

	s9 = 7
	x0 = 4
	paths = []
	try:
		if x <= 2:
			s9 = x*s9
			x0 = 9/x
			paths.append(1)
		else:
			x = x/s9
			paths.append(2)
		if s9 > 5:
			s9 = 9-1
			x0 = x0-s9
			paths.append(3)
		else:
			x = x+1
			paths.append(4)
		paths.append(5)
		assert x >= 0
		x0 = x**0.5
		return x0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))