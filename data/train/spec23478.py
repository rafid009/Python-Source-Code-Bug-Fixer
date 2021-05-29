import numpy as np 

def function(x):

	g1 = x
	y6 = 3
	paths = []
	try:
		if y6 >= 3:
			x = 9/x
			x = 0/3
			paths.append(1)
		else:
			y6 = y6+9
			y6 = y6/2
			y6 = 1-2
			paths.append(2)
		if x >= 5:
			g1 = x/3
			y6 = 8/8
			paths.append(3)
		else:
			x = x-g1
			y6 = x*g1
			x = x+9
			paths.append(4)
		paths.append(5)
		assert g1 >= 0
		x = g1**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))