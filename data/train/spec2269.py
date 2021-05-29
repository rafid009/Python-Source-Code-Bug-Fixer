import numpy as np 

def function(x):

	k5 = x
	y0 = x
	paths = []
	try:
		if k5 <= 2:
			k5 = 4-4
			y0 = x+2
			paths.append(1)
		else:
			y0 = 9/y0
			k5 = k5+k5
			paths.append(2)
		if y0 > 4:
			x = 9-x
			paths.append(3)
		else:
			x = 4/x
			x = x+x
			y0 = 2-y0
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