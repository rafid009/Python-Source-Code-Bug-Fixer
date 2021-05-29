import numpy as np 

def function(x):

	h2 = x
	o4 = 1
	paths = []
	try:
		if o4 > 1:
			h2 = 4/h2
			paths.append(1)
		else:
			x = h2*6
			h2 = 5+h2
			h2 = 9-8
			paths.append(2)
		if o4 > 3:
			x = x-4
			paths.append(3)
		else:
			o4 = 4+x
			o4 = 1+2
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