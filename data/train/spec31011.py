import numpy as np 

def function(x):

	g0 = 5
	x1 = 3
	paths = []
	try:
		if x1 < 2:
			x1 = 6*6
			paths.append(1)
		else:
			x = x*x
			x = x/6
			x1 = 8*x1
			paths.append(2)
		if x1 <= 5:
			g0 = g0*0
			x = 2-x
			paths.append(3)
		else:
			x1 = 1/x
			x = g0-6
			g0 = 1-5
			paths.append(4)
		paths.append(5)
		assert g0 >= 0
		x = g0**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))