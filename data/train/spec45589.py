import numpy as np 

def function(x):

	g4 = 2
	s6 = 0
	paths = []
	try:
		if x <= 4:
			x = x+0
			s6 = g4+1
			paths.append(1)
		else:
			g4 = 2-g4
			x = x+3
			paths.append(2)
		if s6 < 0:
			g4 = 1*g4
			paths.append(3)
		else:
			g4 = 3-9
			s6 = 6+s6
			g4 = g4/g4
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