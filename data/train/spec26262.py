import numpy as np 

def function(x):

	i6 = x
	k0 = 9
	paths = []
	try:
		if x > 7:
			x = k0+5
			k0 = 3/5
			paths.append(1)
		else:
			k0 = 6+k0
			k0 = k0-6
			paths.append(2)
		if i6 < 8:
			k0 = k0/5
			i6 = 2*i6
			x = 8+x
			paths.append(3)
		else:
			x = 2/x
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