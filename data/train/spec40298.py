import numpy as np 

def function(x):

	k0 = 3
	a0 = 3
	x = 8
	paths = []
	try:
		if k0 <= 0:
			k0 = 6/k0
			paths.append(1)
		else:
			x = x*9
			k0 = k0-5
			a0 = x+k0
			paths.append(2)
		if x >= 1:
			a0 = k0*8
			paths.append(3)
		else:
			x = k0-a0
			paths.append(4)
		paths.append(5)
		assert a0 >= 0
		x = a0**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))