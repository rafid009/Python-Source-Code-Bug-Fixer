import numpy as np 

def function(x):

	k5 = x
	a7 = x
	paths = []
	try:
		if k5 <= 8:
			k5 = k5-2
			paths.append(1)
		else:
			x = 1-x
			paths.append(2)
		if x < 2:
			a7 = a7+k5
			a7 = 7-6
			a7 = a7*x
			paths.append(3)
		else:
			a7 = 9+k5
			a7 = x*8
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