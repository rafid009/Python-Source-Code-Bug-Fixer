import numpy as np 

def function(x):

	v5 = x
	x8 = 2
	paths = []
	try:
		if x > 1:
			x = x-7
			x8 = x*x8
			paths.append(1)
		else:
			x8 = x8*x8
			x = 0*x
			paths.append(2)
		if x8 >= 4:
			x = 5+v5
			x = 9+6
			x = x-v5
			paths.append(3)
		else:
			x = v5-4
			paths.append(4)
		paths.append(5)
		assert x8 >= 0
		x = x8**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))