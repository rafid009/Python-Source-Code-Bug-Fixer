import numpy as np 

def function(x):

	a5 = 1
	k0 = x
	paths = []
	try:
		if k0 >= 7:
			a5 = a5/9
			paths.append(1)
		else:
			a5 = 0-a5
			paths.append(2)
		if k0 > 5:
			x = a5+4
			k0 = 7/k0
			paths.append(3)
		else:
			a5 = 3/a5
			paths.append(4)
		paths.append(5)
		assert a5 >= 0
		k0 = a5**0.5
		return k0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))