import numpy as np 

def function(x):

	x1 = 3
	k0 = 3
	paths = []
	try:
		if x1 > 6:
			x = x*1
			paths.append(1)
		else:
			k0 = 3*6
			x1 = 1-x
			paths.append(2)
		if k0 <= 3:
			x1 = x1+x1
			k0 = k0/8
			paths.append(3)
		else:
			k0 = 8+x
			k0 = 7*k0
			x = x-3
			paths.append(4)
		paths.append(5)
		assert x1 >= 0
		x = x1**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))