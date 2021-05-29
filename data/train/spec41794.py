import numpy as np 

def function(x):

	b9 = x
	o7 = 6
	paths = []
	try:
		if b9 < 9:
			o7 = 5*o7
			paths.append(1)
		else:
			b9 = 3/b9
			x = x*b9
			paths.append(2)
		if b9 < 1:
			x = 9/x
			paths.append(3)
		else:
			b9 = b9-1
			b9 = o7-x
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