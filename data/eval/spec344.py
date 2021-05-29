import numpy as np 

def function(x):

	s9 = 9
	x0 = x
	x = x
	paths = []
	try:
		if x0 > 4:
			s9 = x/s9
			s9 = 4*x0
			paths.append(1)
		else:
			s9 = 2-s9
			x = x0-x0
			paths.append(2)
		if s9 > 5:
			x = x+9
			x = x-1
			paths.append(3)
		else:
			x0 = x0-x
			paths.append(4)
		paths.append(5)
		assert x0 >= 0
		x0 = x0**0.5
		return x0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))