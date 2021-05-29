import numpy as np 

def function(x):

	u0 = 9
	g5 = 1
	paths = []
	try:
		if u0 <= 3:
			x = 0-x
			paths.append(1)
		else:
			x = g5*x
			u0 = 0-u0
			u0 = g5/9
			paths.append(2)
		if g5 <= 5:
			g5 = g5+u0
			g5 = 0*7
			paths.append(3)
		else:
			x = 1+x
			x = g5-x
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