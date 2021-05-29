import numpy as np 

def function(x):

	u9 = 3
	g6 = 7
	paths = []
	try:
		if x <= 1:
			u9 = 6+3
			paths.append(1)
		else:
			g6 = 4*x
			paths.append(2)
		if u9 > 9:
			u9 = g6+3
			u9 = g6+u9
			u9 = u9/8
			paths.append(3)
		else:
			u9 = 9/u9
			x = x+6
			u9 = u9+u9
			paths.append(4)
		paths.append(5)
		assert x >= 0
		u9 = x**0.5
		return u9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))