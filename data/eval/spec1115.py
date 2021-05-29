import numpy as np 

def function(x):

	o7 = 2
	x8 = x
	paths = []
	try:
		if x8 > 6:
			o7 = 0/8
			paths.append(1)
		else:
			x = x/x
			paths.append(2)
		if x8 <= 9:
			x = x-4
			paths.append(3)
		else:
			x8 = x-x8
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