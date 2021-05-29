import numpy as np 

def function(x):

	k0 = 3
	k6 = 1
	paths = []
	try:
		if x <= 8:
			k0 = 5+k0
			k6 = k6*k0
			k0 = k0-k6
			paths.append(1)
		else:
			k6 = k6*1
			x = x*4
			paths.append(2)
		if x >= 6:
			k0 = 4-9
			paths.append(3)
		else:
			k0 = k0+1
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