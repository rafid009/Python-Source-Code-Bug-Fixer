import numpy as np 

def function(x):

	i4 = 3
	k0 = 3
	paths = []
	try:
		if k0 <= 0:
			i4 = 2*i4
			k0 = 2*i4
			i4 = 7*i4
			paths.append(1)
		else:
			k0 = k0+3
			i4 = k0-8
			x = x+8
			paths.append(2)
		if k0 >= 8:
			i4 = i4-i4
			i4 = i4/i4
			x = 7+x
			paths.append(3)
		else:
			i4 = i4-4
			paths.append(4)
		paths.append(5)
		assert i4 >= 0
		x = i4**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))