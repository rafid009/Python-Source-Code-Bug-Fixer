import numpy as np 

def function(x):

	u6 = x
	g6 = x
	paths = []
	try:
		if g6 <= 2:
			u6 = 0/u6
			u6 = g6+u6
			paths.append(1)
		else:
			g6 = x/6
			g6 = g6/g6
			paths.append(2)
		if g6 <= 3:
			x = x+9
			paths.append(3)
		else:
			g6 = 5+9
			paths.append(4)
		paths.append(5)
		assert g6 >= 0
		x = g6**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))