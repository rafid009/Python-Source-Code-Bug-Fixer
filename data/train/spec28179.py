import numpy as np 

def function(x):

	g6 = x
	x5 = x
	paths = []
	try:
		if x > 2:
			g6 = 9-1
			x5 = x+x5
			x5 = x5+3
			paths.append(1)
		else:
			x5 = x5+x
			paths.append(2)
		if x5 > 3:
			x5 = x5+x5
			x = x*x
			x = x5-5
			paths.append(3)
		else:
			x5 = 6*0
			paths.append(4)
		paths.append(5)
		assert x >= 0
		x5 = x**0.5
		return x5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))