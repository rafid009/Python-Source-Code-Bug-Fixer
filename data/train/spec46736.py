import numpy as np 

def function(x):

	g5 = x
	r6 = 3
	paths = []
	try:
		if r6 > 9:
			g5 = 5/2
			g5 = 3+0
			x = 0-x
			paths.append(1)
		else:
			r6 = 6/x
			paths.append(2)
		if x <= 0:
			g5 = x+0
			x = g5+r6
			paths.append(3)
		else:
			x = 0-x
			x = 5-x
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