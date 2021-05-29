import numpy as np 

def function(x):

	f5 = x
	g1 = 1
	x = x
	paths = []
	try:
		if f5 <= 8:
			f5 = g1*7
			x = 3/x
			g1 = x+0
			paths.append(1)
		else:
			g1 = g1+7
			paths.append(2)
		if f5 < 6:
			f5 = f5*1
			g1 = 0*g1
			paths.append(3)
		else:
			g1 = 8*g1
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