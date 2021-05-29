import numpy as np 

def function(x):

	e1 = 6
	k0 = x
	paths = []
	try:
		if x >= 9:
			k0 = x-9
			e1 = 1*e1
			paths.append(1)
		else:
			x = 2+x
			paths.append(2)
		if k0 >= 6:
			k0 = k0/8
			paths.append(3)
		else:
			k0 = k0/4
			e1 = e1*x
			paths.append(4)
		paths.append(5)
		assert e1 >= 0
		x = e1**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))