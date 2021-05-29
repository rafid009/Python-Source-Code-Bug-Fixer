import numpy as np 

def function(x):

	k5 = 1
	y6 = x
	paths = []
	try:
		if k5 >= 9:
			x = 0+x
			k5 = k5+k5
			k5 = k5+y6
			paths.append(1)
		else:
			x = 9*x
			k5 = k5/y6
			k5 = x*1
			paths.append(2)
		if x <= 3:
			k5 = 8*x
			paths.append(3)
		else:
			x = x/3
			x = x-5
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