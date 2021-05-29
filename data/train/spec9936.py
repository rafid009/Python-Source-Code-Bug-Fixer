import numpy as np 

def function(x):

	o9 = 4
	o4 = 6
	paths = []
	try:
		if o9 > 8:
			x = o4*x
			o4 = o4-o4
			paths.append(1)
		else:
			o4 = o4/4
			o4 = o4/8
			paths.append(2)
		if o9 > 7:
			o4 = 2-o4
			paths.append(3)
		else:
			o4 = o4-9
			paths.append(4)
		paths.append(5)
		assert o4 >= 0
		o9 = o4**0.5
		return o9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))