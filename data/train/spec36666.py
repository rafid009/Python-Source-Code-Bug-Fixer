import numpy as np 

def function(x):

	z7 = 2
	g2 = x
	paths = []
	try:
		if z7 < 8:
			x = x*5
			x = 6-x
			paths.append(1)
		else:
			x = x*z7
			paths.append(2)
		if g2 <= 8:
			x = 8+x
			paths.append(3)
		else:
			x = 3-x
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