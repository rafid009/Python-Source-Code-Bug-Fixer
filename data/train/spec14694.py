import numpy as np 

def function(x):

	g0 = x
	t7 = x
	x = 8
	paths = []
	try:
		if g0 > 9:
			g0 = g0+1
			g0 = g0+g0
			g0 = g0+t7
			paths.append(1)
		else:
			x = 8+t7
			g0 = 1-5
			t7 = t7*x
			paths.append(2)
		if x > 0:
			g0 = 2+x
			g0 = 1-g0
			paths.append(3)
		else:
			x = 2-8
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