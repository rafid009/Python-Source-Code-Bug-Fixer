import numpy as np 

def function(x):

	k5 = x
	x4 = 3
	paths = []
	try:
		if x <= 6:
			k5 = k5-k5
			paths.append(1)
		else:
			x = 3+k5
			x = x-0
			x = x4/x
			paths.append(2)
		if k5 <= 8:
			k5 = x*k5
			x = x-7
			paths.append(3)
		else:
			k5 = k5/x4
			x4 = 1+6
			x = 7+x
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