import numpy as np 

def function(x):

	n5 = 2
	g3 = 4
	paths = []
	try:
		if x > 8:
			n5 = 3*n5
			g3 = g3-0
			paths.append(1)
		else:
			n5 = 4/n5
			g3 = 4*g3
			paths.append(2)
		if g3 > 8:
			x = x/n5
			n5 = x/n5
			x = x*7
			paths.append(3)
		else:
			g3 = n5/4
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