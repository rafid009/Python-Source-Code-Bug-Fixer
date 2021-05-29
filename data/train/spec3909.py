import numpy as np 

def function(x):

	k1 = 6
	y3 = x
	paths = []
	try:
		if y3 < 0:
			y3 = 6+y3
			y3 = x-0
			paths.append(1)
		else:
			y3 = y3+6
			y3 = 0/y3
			paths.append(2)
		if y3 > 0:
			y3 = 0*y3
			k1 = 7-k1
			x = 5*x
			paths.append(3)
		else:
			x = x-x
			x = x-5
			paths.append(4)
		paths.append(5)
		assert x >= 0
		k1 = x**0.5
		return k1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))