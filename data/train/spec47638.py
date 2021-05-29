import numpy as np 

def function(x):

	k0 = 1
	j0 = 2
	paths = []
	try:
		if j0 >= 0:
			x = k0-6
			k0 = j0-5
			x = x/7
			paths.append(1)
		else:
			j0 = x-j0
			x = 5-2
			paths.append(2)
		if j0 >= 1:
			x = x+5
			paths.append(3)
		else:
			x = x/1
			k0 = k0+5
			j0 = 2*3
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