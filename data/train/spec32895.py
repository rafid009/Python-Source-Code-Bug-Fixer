import numpy as np 

def function(x):

	g0 = 0
	b8 = 5
	paths = []
	try:
		if b8 > 5:
			x = b8+x
			x = x/3
			b8 = 5-b8
			paths.append(1)
		else:
			x = x+1
			g0 = g0*g0
			b8 = 1*3
			paths.append(2)
		if g0 < 6:
			x = x+1
			paths.append(3)
		else:
			b8 = b8-b8
			x = x+2
			g0 = 4-b8
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