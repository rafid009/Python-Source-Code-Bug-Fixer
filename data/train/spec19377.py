import numpy as np 

def function(x):

	o7 = x
	k1 = 3
	paths = []
	try:
		if x < 0:
			x = 1+x
			o7 = 2/k1
			x = x-9
			paths.append(1)
		else:
			k1 = k1*6
			o7 = 0+o7
			paths.append(2)
		if x <= 1:
			o7 = o7-1
			paths.append(3)
		else:
			x = 4+3
			paths.append(4)
		paths.append(5)
		assert x >= 0
		o7 = x**0.5
		return o7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))