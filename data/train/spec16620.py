import numpy as np 

def function(x):

	l3 = 4
	g0 = x
	paths = []
	try:
		if g0 < 0:
			l3 = 4/9
			g0 = 6/g0
			paths.append(1)
		else:
			x = x-4
			g0 = l3-g0
			l3 = x*l3
			paths.append(2)
		if l3 <= 1:
			g0 = x*x
			paths.append(3)
		else:
			x = 7*g0
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