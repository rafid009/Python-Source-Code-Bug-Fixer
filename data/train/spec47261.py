import numpy as np 

def function(x):

	d1 = 9
	g5 = 8
	paths = []
	try:
		if d1 >= 0:
			x = x*5
			x = d1/9
			paths.append(1)
		else:
			g5 = 5*g5
			paths.append(2)
		if d1 <= 8:
			x = x/2
			paths.append(3)
		else:
			x = x-4
			d1 = 3/d1
			paths.append(4)
		paths.append(5)
		assert x >= 0
		g5 = x**0.5
		return g5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))