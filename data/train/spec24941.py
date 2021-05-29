import numpy as np 

def function(x):

	k5 = 1
	r9 = x
	x = 6
	paths = []
	try:
		if x > 9:
			k5 = x+k5
			x = x*x
			paths.append(1)
		else:
			r9 = 4/r9
			paths.append(2)
		if k5 > 6:
			r9 = r9/k5
			paths.append(3)
		else:
			x = k5-3
			r9 = x/8
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