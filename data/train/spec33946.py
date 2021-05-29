import numpy as np 

def function(x):

	u6 = 3
	g5 = x
	paths = []
	try:
		if u6 >= 8:
			g5 = x/g5
			x = x/7
			paths.append(1)
		else:
			g5 = u6-g5
			paths.append(2)
		if x >= 0:
			u6 = 5+g5
			paths.append(3)
		else:
			g5 = 8/9
			x = x+g5
			paths.append(4)
		paths.append(5)
		assert g5 >= 0
		g5 = g5**0.5
		return g5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))