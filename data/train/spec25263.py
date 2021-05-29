import numpy as np 

def function(x):

	g1 = x
	p8 = 5
	paths = []
	try:
		if x < 0:
			x = g1-6
			x = 1+x
			paths.append(1)
		else:
			p8 = x/5
			p8 = p8/g1
			p8 = 4-0
			paths.append(2)
		if x > 0:
			x = x/5
			g1 = 0+g1
			x = x/8
			paths.append(3)
		else:
			g1 = 8/g1
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