import numpy as np 

def function(x):

	h2 = 2
	k0 = x
	paths = []
	try:
		if k0 >= 1:
			x = 5+x
			x = 0+2
			paths.append(1)
		else:
			k0 = 3/8
			paths.append(2)
		if h2 <= 4:
			x = x+x
			k0 = k0+2
			k0 = 0-k0
			paths.append(3)
		else:
			x = h2-h2
			h2 = 8/h2
			paths.append(4)
		paths.append(5)
		assert k0 >= 0
		x = k0**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))