import numpy as np 

def function(x):

	k0 = x
	e8 = 3
	paths = []
	try:
		if x >= 4:
			k0 = e8-9
			x = x+7
			k0 = x/e8
			paths.append(1)
		else:
			e8 = 6/e8
			k0 = k0-5
			paths.append(2)
		if e8 >= 4:
			k0 = 4/x
			k0 = 9/e8
			x = 1*9
			paths.append(3)
		else:
			k0 = k0/7
			e8 = e8+2
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