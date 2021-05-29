import numpy as np 

def function(x):

	k6 = 2
	r1 = x
	paths = []
	try:
		if r1 > 4:
			r1 = 0-k6
			x = 1+2
			paths.append(1)
		else:
			k6 = x-4
			paths.append(2)
		if k6 > 9:
			x = x+7
			r1 = 7/r1
			k6 = 1-k6
			paths.append(3)
		else:
			k6 = 3-9
			r1 = 3/r1
			k6 = 0/k6
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