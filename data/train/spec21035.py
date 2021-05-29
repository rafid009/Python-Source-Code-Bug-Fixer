import numpy as np 

def function(x):

	v9 = x
	k7 = 0
	paths = []
	try:
		if v9 < 1:
			x = x+6
			paths.append(1)
		else:
			k7 = 7+k7
			paths.append(2)
		if k7 < 1:
			k7 = k7-9
			paths.append(3)
		else:
			k7 = k7-v9
			x = 4*x
			paths.append(4)
		paths.append(5)
		assert x >= 0
		v9 = x**0.5
		return v9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))