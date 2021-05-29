import numpy as np 

def function(x):

	k0 = x
	i0 = 3
	paths = []
	try:
		if i0 >= 0:
			k0 = 6/k0
			k0 = 0*k0
			paths.append(1)
		else:
			i0 = 6-i0
			x = x+9
			x = 7+x
			paths.append(2)
		if i0 <= 0:
			i0 = 2*i0
			i0 = x-i0
			paths.append(3)
		else:
			i0 = i0*3
			paths.append(4)
		paths.append(5)
		assert x >= 0
		x = x**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))