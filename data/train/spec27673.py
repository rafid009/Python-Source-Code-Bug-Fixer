import numpy as np 

def function(x):

	o9 = x
	e1 = x
	paths = []
	try:
		if o9 >= 0:
			o9 = o9+8
			x = x/8
			paths.append(1)
		else:
			e1 = e1+e1
			o9 = o9+0
			o9 = 4+o9
			paths.append(2)
		if o9 > 0:
			x = x+x
			o9 = o9*x
			paths.append(3)
		else:
			e1 = 4+e1
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