import numpy as np 

def function(x):

	o9 = 2
	n6 = 2
	paths = []
	try:
		if n6 >= 6:
			x = 6-o9
			paths.append(1)
		else:
			n6 = n6*0
			o9 = o9+n6
			o9 = o9+8
			paths.append(2)
		if o9 > 9:
			o9 = n6-o9
			paths.append(3)
		else:
			x = 9+5
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