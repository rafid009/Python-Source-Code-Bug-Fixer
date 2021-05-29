import numpy as np 

def function(x):

	i2 = x
	g5 = x
	paths = []
	try:
		if g5 > 0:
			x = x*g5
			i2 = 9+i2
			g5 = g5/8
			paths.append(1)
		else:
			i2 = i2-2
			g5 = 3*x
			paths.append(2)
		if g5 <= 7:
			x = 4+6
			i2 = 2*g5
			paths.append(3)
		else:
			x = g5+i2
			g5 = g5/x
			i2 = 3/i2
			paths.append(4)
		paths.append(5)
		assert i2 >= 0
		g5 = i2**0.5
		return g5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))