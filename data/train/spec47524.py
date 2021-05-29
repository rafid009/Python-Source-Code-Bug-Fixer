import numpy as np 

def function(x):

	y1 = x
	k0 = 8
	paths = []
	try:
		if x <= 0:
			x = 7*x
			paths.append(1)
		else:
			y1 = 8*8
			paths.append(2)
		if x >= 4:
			k0 = 3-k0
			k0 = k0+k0
			paths.append(3)
		else:
			k0 = 0/4
			k0 = 1*y1
			k0 = k0+k0
			paths.append(4)
		paths.append(5)
		assert k0 >= 0
		y1 = k0**0.5
		return y1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))