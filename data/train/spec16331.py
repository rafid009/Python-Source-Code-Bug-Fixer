import numpy as np 

def function(x):

	o9 = x
	d5 = 2
	paths = []
	try:
		if d5 > 5:
			x = 5/4
			paths.append(1)
		else:
			o9 = 1*9
			paths.append(2)
		if o9 <= 3:
			x = 5-8
			o9 = o9-5
			x = x-5
			paths.append(3)
		else:
			o9 = 8-o9
			o9 = 4+o9
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