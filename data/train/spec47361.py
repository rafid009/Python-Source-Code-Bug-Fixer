import numpy as np 

def function(x):

	x1 = 2
	g1 = 0
	paths = []
	try:
		if x > 8:
			x = x1-x1
			g1 = g1+5
			x1 = 1+3
			paths.append(1)
		else:
			x1 = x*x1
			paths.append(2)
		if g1 <= 8:
			x = 3-x
			g1 = 4+g1
			paths.append(3)
		else:
			x = g1*0
			g1 = x1-4
			g1 = 8*3
			paths.append(4)
		paths.append(5)
		assert x1 >= 0
		g1 = x1**0.5
		return g1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))