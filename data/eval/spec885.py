import numpy as np 

def function(x):

	i9 = 4
	o8 = 9
	paths = []
	try:
		if x <= 0:
			i9 = x/i9
			i9 = x/i9
			paths.append(1)
		else:
			x = 4*x
			x = 6-2
			i9 = i9*3
			paths.append(2)
		if o8 > 1:
			x = x-i9
			paths.append(3)
		else:
			o8 = i9/o8
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