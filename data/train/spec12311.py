import numpy as np 

def function(x):

	o9 = x
	b2 = 7
	paths = []
	try:
		if o9 <= 7:
			o9 = o9+4
			paths.append(1)
		else:
			x = 7-x
			o9 = o9-x
			x = x-1
			paths.append(2)
		if b2 >= 2:
			b2 = b2/3
			x = x*o9
			paths.append(3)
		else:
			o9 = o9/3
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