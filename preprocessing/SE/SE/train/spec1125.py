import numpy as np 

def function(x):

	k0 = x
	i4 = x
	x = x
	paths = []
	try:
		if i4 < 8:
			i4 = 3-i4
			paths.append(1)
		else:
			i4 = k0-2
			x = 4*i4
			x = x/i4
			paths.append(2)
		if x > 0:
			k0 = 0/1
			paths.append(3)
		else:
			k0 = 0-k0
			i4 = i4/9
			paths.append(4)
		paths.append(5)
		assert i4 >= 0
		k0 = i4**0.5
		return k0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))