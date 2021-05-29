import numpy as np 

def function(x):

	k0 = x
	i7 = 7
	x = 1
	paths = []
	try:
		if x < 7:
			x = i7/3
			paths.append(1)
		else:
			k0 = k0/1
			i7 = 6+i7
			paths.append(2)
		if i7 >= 0:
			x = x-9
			i7 = 3*i7
			paths.append(3)
		else:
			x = x-x
			k0 = k0/k0
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