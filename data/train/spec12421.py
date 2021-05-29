import numpy as np 

def function(x):

	s6 = 9
	g3 = 4
	x = x
	paths = []
	try:
		if x <= 5:
			x = x+x
			g3 = 4*5
			paths.append(1)
		else:
			x = 2-9
			paths.append(2)
		if x >= 1:
			g3 = g3/s6
			s6 = 6/g3
			g3 = g3-x
			paths.append(3)
		else:
			s6 = x+s6
			x = g3/x
			x = x+0
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