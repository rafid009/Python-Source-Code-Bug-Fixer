import numpy as np 

def function(x):

	k5 = 9
	z4 = 2
	paths = []
	try:
		if z4 <= 6:
			k5 = 8/k5
			paths.append(1)
		else:
			k5 = k5+8
			paths.append(2)
		if k5 > 6:
			x = 2+x
			paths.append(3)
		else:
			x = z4/x
			paths.append(4)
		paths.append(5)
		assert x >= 0
		k5 = x**0.5
		return k5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))