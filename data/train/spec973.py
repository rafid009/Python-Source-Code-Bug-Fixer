import numpy as np 

def function(x):

	g6 = 6
	u1 = x
	paths = []
	try:
		if x <= 8:
			x = 1+8
			u1 = u1*1
			g6 = u1-g6
			paths.append(1)
		else:
			u1 = g6-u1
			g6 = x*5
			g6 = x+g6
			paths.append(2)
		if x > 4:
			u1 = 7/u1
			x = g6/7
			paths.append(3)
		else:
			u1 = u1/2
			x = 8+u1
			paths.append(4)
		paths.append(5)
		assert g6 >= 0
		g6 = g6**0.5
		return g6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))