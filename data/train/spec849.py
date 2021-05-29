import numpy as np 

def function(x):

	r7 = x
	s7 = 5
	paths = []
	try:
		if r7 < 8:
			x = x/2
			x = x/5
			paths.append(1)
		else:
			x = 1-4
			paths.append(2)
		if r7 < 8:
			s7 = 9/4
			paths.append(3)
		else:
			x = 4*r7
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