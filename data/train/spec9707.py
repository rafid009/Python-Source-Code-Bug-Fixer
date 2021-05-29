import numpy as np 

def function(x):

	k0 = x
	l1 = 3
	paths = []
	try:
		if l1 < 8:
			k0 = k0+4
			x = 4-x
			paths.append(1)
		else:
			x = 6*x
			x = 7*9
			k0 = k0+k0
			paths.append(2)
		if x >= 8:
			x = x+x
			paths.append(3)
		else:
			k0 = 4/7
			l1 = 5+k0
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