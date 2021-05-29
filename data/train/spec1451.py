import numpy as np 

def function(x):

	z4 = 0
	o4 = x
	paths = []
	try:
		if x > 1:
			o4 = 2/o4
			paths.append(1)
		else:
			x = 2+x
			paths.append(2)
		if z4 <= 4:
			x = x-z4
			paths.append(3)
		else:
			o4 = o4/4
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