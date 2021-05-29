import numpy as np 

def function(x):

	u6 = x
	g6 = 3
	paths = []
	try:
		if u6 >= 5:
			u6 = 0+u6
			g6 = u6/6
			paths.append(1)
		else:
			x = 8+x
			paths.append(2)
		if x >= 7:
			u6 = 4-6
			paths.append(3)
		else:
			x = 2/x
			g6 = g6*5
			paths.append(4)
		paths.append(5)
		assert x >= 0
		u6 = x**0.5
		return u6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))