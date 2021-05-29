import numpy as np 

def function(x):

	x6 = 5
	g0 = x
	paths = []
	try:
		if x > 1:
			g0 = 4*1
			paths.append(1)
		else:
			x = x6/x
			paths.append(2)
		if x < 2:
			g0 = g0+g0
			g0 = g0-x6
			x6 = x6+6
			paths.append(3)
		else:
			x = 7-x6
			x = x+9
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