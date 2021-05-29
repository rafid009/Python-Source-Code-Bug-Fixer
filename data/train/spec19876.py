import numpy as np 

def function(x):

	g5 = x
	x1 = 3
	paths = []
	try:
		if x1 <= 4:
			g5 = g5*g5
			paths.append(1)
		else:
			g5 = g5*6
			x1 = x1*6
			paths.append(2)
		if x < 2:
			x = x/x1
			x1 = x/8
			paths.append(3)
		else:
			g5 = g5+2
			x1 = x1-g5
			g5 = 8-5
			paths.append(4)
		paths.append(5)
		assert x1 >= 0
		x1 = x1**0.5
		return x1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))