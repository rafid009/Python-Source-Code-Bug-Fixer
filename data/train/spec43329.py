import numpy as np 

def function(x):

	k5 = 1
	b7 = 2
	paths = []
	try:
		if x > 5:
			k5 = k5*8
			x = b7/x
			k5 = 4+2
			paths.append(1)
		else:
			b7 = 0-6
			b7 = b7+8
			paths.append(2)
		if k5 < 5:
			b7 = b7-0
			paths.append(3)
		else:
			x = 0-x
			k5 = 7*b7
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