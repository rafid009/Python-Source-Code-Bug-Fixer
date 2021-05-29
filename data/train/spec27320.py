import numpy as np 

def function(x):

	o4 = x
	b2 = x
	paths = []
	try:
		if o4 >= 2:
			b2 = b2-3
			paths.append(1)
		else:
			b2 = b2-8
			paths.append(2)
		if o4 <= 5:
			b2 = 7/2
			o4 = o4+4
			b2 = 9/o4
			paths.append(3)
		else:
			x = 4/8
			b2 = 3/7
			o4 = 6/x
			paths.append(4)
		paths.append(5)
		assert x >= 0
		o4 = x**0.5
		return o4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))