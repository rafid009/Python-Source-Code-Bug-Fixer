import numpy as np 

def function(x):

	g4 = x
	s5 = x
	x = x
	paths = []
	try:
		if g4 >= 5:
			g4 = 6+s5
			s5 = 9+s5
			x = 6+x
			paths.append(1)
		else:
			x = 2+x
			g4 = 4-g4
			paths.append(2)
		if x < 4:
			g4 = g4/g4
			s5 = s5/8
			x = 1/x
			paths.append(3)
		else:
			x = 4+0
			x = 9-g4
			paths.append(4)
		paths.append(5)
		assert x >= 0
		g4 = x**0.5
		return g4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))