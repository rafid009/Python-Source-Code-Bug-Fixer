import numpy as np 

def function(x):

	g2 = 3
	s1 = x
	paths = []
	try:
		if g2 >= 2:
			x = 3/x
			x = 3-x
			paths.append(1)
		else:
			g2 = g2/x
			paths.append(2)
		if g2 <= 6:
			g2 = 6*6
			paths.append(3)
		else:
			x = g2/g2
			g2 = g2*s1
			s1 = x*9
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