import numpy as np 

def function(x):

	k0 = x
	y7 = 6
	paths = []
	try:
		if x > 3:
			k0 = x/k0
			k0 = k0*1
			paths.append(1)
		else:
			x = x+y7
			paths.append(2)
		if y7 >= 0:
			y7 = k0*1
			k0 = k0/1
			y7 = 4+y7
			paths.append(3)
		else:
			y7 = 8-y7
			x = x-4
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