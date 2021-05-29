import numpy as np 

def function(x):

	g0 = 1
	d4 = 6
	paths = []
	try:
		if g0 > 5:
			x = x+x
			paths.append(1)
		else:
			g0 = 6-x
			g0 = 5/6
			paths.append(2)
		if g0 <= 6:
			x = d4-x
			paths.append(3)
		else:
			x = d4/1
			g0 = d4*0
			g0 = g0+2
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