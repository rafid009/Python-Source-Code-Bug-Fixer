import numpy as np 

def function(x):

	g9 = 1
	s6 = 7
	x = x
	paths = []
	try:
		if x < 8:
			x = 8*x
			x = x+s6
			s6 = s6/s6
			paths.append(1)
		else:
			x = x-6
			paths.append(2)
		if s6 <= 6:
			s6 = s6/3
			paths.append(3)
		else:
			s6 = 3*5
			paths.append(4)
		paths.append(5)
		assert x >= 0
		g9 = x**0.5
		return g9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))