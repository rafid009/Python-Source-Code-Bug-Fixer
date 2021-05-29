import numpy as np 

def function(x):

	o9 = x
	n6 = x
	paths = []
	try:
		if o9 < 1:
			o9 = o9+5
			paths.append(1)
		else:
			x = x+9
			n6 = 8-x
			o9 = 5-o9
			paths.append(2)
		if x < 9:
			n6 = o9-n6
			o9 = o9+n6
			paths.append(3)
		else:
			x = x/x
			n6 = n6+x
			x = x-6
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