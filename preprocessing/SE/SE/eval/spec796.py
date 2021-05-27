import numpy as np 

def function(x):

	k1 = 5
	e0 = x
	paths = []
	try:
		if x >= 2:
			x = 9*x
			paths.append(1)
		else:
			x = 3+k1
			k1 = 6+2
			k1 = 7/k1
			paths.append(2)
		if k1 < 6:
			x = e0-x
			x = x-k1
			k1 = k1*k1
			paths.append(3)
		else:
			x = x-x
			k1 = k1+0
			paths.append(4)
		paths.append(5)
		assert e0 >= 0
		e0 = e0**0.5
		return e0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))