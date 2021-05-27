import numpy as np 

def function(x):

	g0 = 4
	e0 = 8
	paths = []
	try:
		if g0 <= 9:
			g0 = g0/4
			e0 = 8+1
			e0 = 8*e0
			paths.append(1)
		else:
			e0 = 8/1
			x = 3/2
			paths.append(2)
		if x > 3:
			e0 = 8+0
			e0 = e0*e0
			x = x+5
			paths.append(3)
		else:
			x = x/6
			e0 = x*8
			e0 = 7-9
			paths.append(4)
		paths.append(5)
		assert x >= 0
		g0 = x**0.5
		return g0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))