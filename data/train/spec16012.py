import numpy as np 

def function(x):

	g1 = x
	h3 = x
	paths = []
	try:
		if g1 >= 4:
			h3 = g1/4
			x = x-5
			h3 = x*g1
			paths.append(1)
		else:
			h3 = 5+1
			g1 = g1/9
			paths.append(2)
		if x <= 1:
			h3 = 5/3
			x = 1/g1
			paths.append(3)
		else:
			x = x+1
			g1 = h3+7
			paths.append(4)
		paths.append(5)
		assert x >= 0
		g1 = x**0.5
		return g1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))