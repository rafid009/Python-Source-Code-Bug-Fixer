import numpy as np 

def function(x):

	g5 = 2
	u3 = x
	paths = []
	try:
		if x > 1:
			u3 = 2-x
			g5 = 3*9
			paths.append(1)
		else:
			u3 = 5/3
			paths.append(2)
		if g5 >= 0:
			g5 = g5-1
			x = x-1
			x = g5-x
			paths.append(3)
		else:
			x = x/3
			paths.append(4)
		paths.append(5)
		assert x >= 0
		g5 = x**0.5
		return g5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))