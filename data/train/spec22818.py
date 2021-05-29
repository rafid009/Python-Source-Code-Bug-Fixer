import numpy as np 

def function(x):

	b3 = x
	o9 = x
	x = 6
	paths = []
	try:
		if b3 > 6:
			b3 = b3-9
			paths.append(1)
		else:
			x = x-x
			paths.append(2)
		if o9 > 1:
			b3 = 9*9
			paths.append(3)
		else:
			b3 = b3*3
			x = 4/b3
			o9 = o9-8
			paths.append(4)
		paths.append(5)
		assert x >= 0
		o9 = x**0.5
		return o9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))