import numpy as np 

def function(x):

	g0 = 8
	u3 = 4
	paths = []
	try:
		if u3 <= 7:
			u3 = x/4
			u3 = u3/u3
			paths.append(1)
		else:
			x = 0-1
			x = 9*4
			x = x+5
			paths.append(2)
		if g0 < 0:
			u3 = 6*x
			x = 0-x
			paths.append(3)
		else:
			g0 = g0*x
			g0 = g0*g0
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