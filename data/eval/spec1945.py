import numpy as np 

def function(x):

	g5 = x
	o9 = 4
	paths = []
	try:
		if o9 < 6:
			g5 = 4-g5
			paths.append(1)
		else:
			x = 2-6
			x = x-9
			g5 = 2*x
			paths.append(2)
		if g5 >= 8:
			g5 = 6/g5
			x = x*0
			g5 = 2*g5
			paths.append(3)
		else:
			x = x/1
			g5 = g5+3
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