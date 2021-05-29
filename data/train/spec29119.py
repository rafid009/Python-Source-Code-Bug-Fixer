import numpy as np 

def function(x):

	o6 = 5
	a9 = x
	paths = []
	try:
		if o6 <= 8:
			a9 = o6*2
			a9 = a9-6
			paths.append(1)
		else:
			a9 = 2*9
			a9 = 3/a9
			o6 = a9-8
			paths.append(2)
		if x < 5:
			o6 = 9+8
			o6 = o6+4
			a9 = 6*a9
			paths.append(3)
		else:
			o6 = a9*o6
			a9 = 0-3
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