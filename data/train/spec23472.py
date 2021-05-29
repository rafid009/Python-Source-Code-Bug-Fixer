import numpy as np 

def function(x):

	g3 = 4
	y9 = 6
	paths = []
	try:
		if g3 > 1:
			g3 = 4/g3
			y9 = y9/6
			g3 = g3/1
			paths.append(1)
		else:
			g3 = g3+0
			g3 = g3+y9
			paths.append(2)
		if x > 5:
			g3 = x+g3
			x = 4*9
			g3 = 1/g3
			paths.append(3)
		else:
			y9 = 2+y9
			x = x+9
			paths.append(4)
		paths.append(5)
		assert x >= 0
		y9 = x**0.5
		return y9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))