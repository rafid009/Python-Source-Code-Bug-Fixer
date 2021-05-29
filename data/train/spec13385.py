import numpy as np 

def function(x):

	g9 = x
	f7 = 2
	paths = []
	try:
		if x <= 2:
			g9 = f7/g9
			paths.append(1)
		else:
			x = 9-2
			g9 = g9*g9
			x = 1-x
			paths.append(2)
		if g9 > 0:
			g9 = g9-5
			x = x+x
			paths.append(3)
		else:
			x = x/2
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