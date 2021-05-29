import numpy as np 

def function(x):

	g7 = 1
	n4 = x
	paths = []
	try:
		if n4 >= 6:
			n4 = n4/x
			paths.append(1)
		else:
			g7 = 8/g7
			paths.append(2)
		if g7 <= 3:
			g7 = g7+7
			x = x-7
			g7 = 5-g7
			paths.append(3)
		else:
			g7 = g7/4
			g7 = g7*0
			paths.append(4)
		paths.append(5)
		assert x >= 0
		n4 = x**0.5
		return n4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))