import numpy as np 

def function(x):

	k0 = 8
	y6 = 5
	paths = []
	try:
		if x > 9:
			k0 = 0+x
			k0 = k0/5
			x = 4-x
			paths.append(1)
		else:
			k0 = 9*5
			k0 = x+0
			k0 = 3+k0
			paths.append(2)
		if x > 7:
			k0 = k0*x
			k0 = k0/k0
			paths.append(3)
		else:
			y6 = x+y6
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