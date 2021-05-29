import numpy as np 

def function(x):

	o2 = 7
	g9 = 9
	paths = []
	try:
		if g9 > 0:
			g9 = g9/g9
			g9 = 9-g9
			paths.append(1)
		else:
			o2 = o2*x
			x = 3*x
			paths.append(2)
		if x > 9:
			g9 = 3+g9
			x = x+0
			paths.append(3)
		else:
			o2 = o2-2
			g9 = g9-g9
			g9 = 0-x
			paths.append(4)
		paths.append(5)
		assert x >= 0
		x = x**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))