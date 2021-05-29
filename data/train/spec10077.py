import numpy as np 

def function(x):

	k0 = x
	x3 = 3
	paths = []
	try:
		if k0 > 6:
			x3 = 3/1
			paths.append(1)
		else:
			x = x3-1
			x3 = x3*x3
			paths.append(2)
		if x > 4:
			k0 = k0-0
			x3 = x3/8
			paths.append(3)
		else:
			x3 = x3/3
			paths.append(4)
		paths.append(5)
		assert k0 >= 0
		x3 = k0**0.5
		return x3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))