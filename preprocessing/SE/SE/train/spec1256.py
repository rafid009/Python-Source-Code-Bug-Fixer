import numpy as np 

def function(x):

	g5 = 9
	d9 = 6
	paths = []
	try:
		if g5 <= 7:
			g5 = x*d9
			d9 = 3*5
			paths.append(1)
		else:
			g5 = 3/x
			x = x/9
			paths.append(2)
		if x < 3:
			g5 = g5*1
			g5 = g5-6
			paths.append(3)
		else:
			d9 = d9+4
			x = g5*x
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