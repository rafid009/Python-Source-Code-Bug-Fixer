import numpy as np 

def function(x):

	r9 = 9
	k0 = 5
	paths = []
	try:
		if k0 > 9:
			k0 = 5+r9
			x = r9+x
			k0 = k0+x
			paths.append(1)
		else:
			r9 = x+9
			paths.append(2)
		if k0 <= 5:
			x = 7*x
			paths.append(3)
		else:
			r9 = 9-r9
			k0 = k0-6
			r9 = 9+k0
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