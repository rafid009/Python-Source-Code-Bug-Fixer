import numpy as np 

def function(x):

	g3 = 9
	s9 = 7
	paths = []
	try:
		if g3 < 2:
			s9 = 2/s9
			x = x/x
			paths.append(1)
		else:
			x = x*s9
			x = 7*x
			paths.append(2)
		if g3 < 1:
			s9 = 3*s9
			x = x/3
			paths.append(3)
		else:
			s9 = s9-9
			x = s9*x
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