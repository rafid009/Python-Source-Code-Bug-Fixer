import numpy as np 

def function(x):

	k0 = 6
	y8 = x
	paths = []
	try:
		if y8 < 1:
			x = 8*x
			paths.append(1)
		else:
			x = x-9
			k0 = x*3
			paths.append(2)
		if k0 > 9:
			k0 = x+k0
			paths.append(3)
		else:
			y8 = y8/k0
			k0 = 1/k0
			y8 = 4/3
			paths.append(4)
		paths.append(5)
		assert x >= 0
		y8 = x**0.5
		return y8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))