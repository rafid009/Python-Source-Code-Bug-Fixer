import numpy as np 

def function(x):

	l7 = 2
	k0 = 7
	paths = []
	try:
		if k0 >= 8:
			x = x*7
			paths.append(1)
		else:
			x = 3+x
			paths.append(2)
		if k0 <= 2:
			k0 = k0-x
			paths.append(3)
		else:
			k0 = 2/k0
			paths.append(4)
		paths.append(5)
		assert x >= 0
		l7 = x**0.5
		return l7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))