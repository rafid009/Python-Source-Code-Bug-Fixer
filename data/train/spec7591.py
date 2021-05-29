import numpy as np 

def function(x):

	k3 = 6
	y6 = 9
	paths = []
	try:
		if y6 < 7:
			y6 = k3/y6
			paths.append(1)
		else:
			y6 = k3/k3
			paths.append(2)
		if y6 > 9:
			k3 = k3*k3
			y6 = 8/1
			paths.append(3)
		else:
			x = x+y6
			y6 = y6*y6
			paths.append(4)
		paths.append(5)
		assert x >= 0
		y6 = x**0.5
		return y6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))