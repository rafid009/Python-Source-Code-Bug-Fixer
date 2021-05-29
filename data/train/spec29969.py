import numpy as np 

def function(x):

	g3 = x
	x9 = x
	paths = []
	try:
		if x9 < 7:
			x = x*x
			x = g3/x
			x = x9+x
			paths.append(1)
		else:
			x9 = 1+4
			x = g3-6
			paths.append(2)
		if g3 > 7:
			g3 = g3-6
			paths.append(3)
		else:
			x = x*x
			g3 = x9*x
			paths.append(4)
		paths.append(5)
		assert x9 >= 0
		x9 = x9**0.5
		return x9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))