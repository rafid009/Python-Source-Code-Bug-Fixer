import numpy as np 

def function(x):

	g1 = 5
	r7 = x
	paths = []
	try:
		if g1 < 9:
			g1 = 1+0
			paths.append(1)
		else:
			g1 = g1/7
			g1 = g1/2
			paths.append(2)
		if g1 <= 9:
			g1 = 4+x
			paths.append(3)
		else:
			r7 = r7+3
			x = x-2
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