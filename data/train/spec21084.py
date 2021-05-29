import numpy as np 

def function(x):

	o4 = 1
	n1 = 4
	x = 3
	paths = []
	try:
		if x <= 2:
			o4 = x-2
			n1 = 9+o4
			x = x-5
			paths.append(1)
		else:
			x = o4/9
			x = x*o4
			x = 9+o4
			paths.append(2)
		if o4 >= 1:
			n1 = n1-5
			o4 = o4-3
			paths.append(3)
		else:
			n1 = n1+3
			paths.append(4)
		paths.append(5)
		assert o4 >= 0
		o4 = o4**0.5
		return o4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))