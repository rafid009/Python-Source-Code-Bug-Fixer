import numpy as np 

def function(x):

	g0 = 7
	s9 = x
	paths = []
	try:
		if g0 <= 5:
			g0 = x+g0
			paths.append(1)
		else:
			g0 = 0-g0
			paths.append(2)
		if s9 > 0:
			x = 1-x
			g0 = g0*s9
			g0 = g0*5
			paths.append(3)
		else:
			x = 9-x
			paths.append(4)
		paths.append(5)
		assert s9 >= 0
		x = s9**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))