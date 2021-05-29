import numpy as np 

def function(x):

	k0 = 9
	u1 = 3
	paths = []
	try:
		if u1 > 6:
			u1 = u1/u1
			k0 = k0-u1
			k0 = x-x
			paths.append(1)
		else:
			u1 = x/k0
			paths.append(2)
		if u1 <= 8:
			u1 = 4*1
			paths.append(3)
		else:
			u1 = 1/u1
			x = x/8
			u1 = 5-u1
			paths.append(4)
		paths.append(5)
		assert x >= 0
		k0 = x**0.5
		return k0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))