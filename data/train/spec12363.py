import numpy as np 

def function(x):

	k0 = x
	f1 = x
	paths = []
	try:
		if f1 <= 2:
			f1 = k0+3
			k0 = k0+x
			paths.append(1)
		else:
			f1 = 1-f1
			paths.append(2)
		if k0 >= 7:
			x = x-7
			paths.append(3)
		else:
			k0 = 9/k0
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