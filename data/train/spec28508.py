import numpy as np 

def function(x):

	s6 = x
	z1 = 2
	paths = []
	try:
		if x < 0:
			x = x-6
			x = 6-x
			paths.append(1)
		else:
			x = x+3
			paths.append(2)
		if s6 > 9:
			s6 = z1+5
			paths.append(3)
		else:
			x = x*s6
			x = x+z1
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