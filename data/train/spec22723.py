import numpy as np 

def function(x):

	f8 = x
	k0 = x
	paths = []
	try:
		if x < 4:
			f8 = 3/f8
			paths.append(1)
		else:
			x = 3/1
			f8 = f8+k0
			k0 = 5/3
			paths.append(2)
		if x <= 6:
			x = f8/2
			k0 = f8*7
			f8 = f8+2
			paths.append(3)
		else:
			k0 = 4/k0
			x = x-f8
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