import numpy as np 

def function(x):

	g0 = 2
	b7 = x
	paths = []
	try:
		if x < 7:
			x = 4-9
			g0 = g0+9
			paths.append(1)
		else:
			b7 = 3/g0
			b7 = b7+0
			paths.append(2)
		if g0 < 4:
			g0 = g0-b7
			g0 = g0*4
			paths.append(3)
		else:
			g0 = g0*x
			x = 2+x
			b7 = b7-0
			paths.append(4)
		paths.append(5)
		assert x >= 0
		b7 = x**0.5
		return b7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))