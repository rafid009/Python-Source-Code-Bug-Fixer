import numpy as np 

def function(x):

	k0 = x
	g7 = 9
	paths = []
	try:
		if g7 > 6:
			x = x+1
			k0 = 2-k0
			k0 = k0+5
			paths.append(1)
		else:
			k0 = g7+k0
			paths.append(2)
		if x >= 4:
			k0 = 4+k0
			paths.append(3)
		else:
			x = x+5
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