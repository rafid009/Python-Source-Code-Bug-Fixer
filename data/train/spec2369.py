import numpy as np 

def function(x):

	x2 = 8
	g0 = 4
	paths = []
	try:
		if x < 4:
			x2 = x+g0
			paths.append(1)
		else:
			g0 = 8+x2
			paths.append(2)
		if g0 > 5:
			g0 = x*3
			paths.append(3)
		else:
			g0 = g0*2
			x2 = x+g0
			paths.append(4)
		paths.append(5)
		assert x >= 0
		x2 = x**0.5
		return x2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))