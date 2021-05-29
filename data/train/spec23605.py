import numpy as np 

def function(x):

	y6 = 2
	k5 = 5
	paths = []
	try:
		if y6 < 7:
			k5 = 4+k5
			x = 9+x
			k5 = k5-y6
			paths.append(1)
		else:
			k5 = k5-k5
			paths.append(2)
		if y6 < 3:
			k5 = 2*1
			k5 = 0*y6
			paths.append(3)
		else:
			k5 = k5/k5
			x = x*y6
			x = x/2
			paths.append(4)
		paths.append(5)
		assert x >= 0
		x = x**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))