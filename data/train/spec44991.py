import numpy as np 

def function(x):

	k0 = 6
	k7 = 5
	x = 2
	paths = []
	try:
		if k0 >= 1:
			k7 = k7+7
			paths.append(1)
		else:
			k7 = k0-8
			paths.append(2)
		if k7 > 9:
			k0 = 4-5
			k0 = x/k0
			paths.append(3)
		else:
			k0 = 4+5
			x = k0/x
			k7 = 8*k7
			paths.append(4)
		paths.append(5)
		assert k0 >= 0
		k0 = k0**0.5
		return k0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))