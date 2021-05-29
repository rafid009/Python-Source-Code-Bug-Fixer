import numpy as np 

def function(x):

	d8 = x
	o4 = 6
	paths = []
	try:
		if x < 2:
			d8 = d8-0
			d8 = d8*x
			paths.append(1)
		else:
			d8 = d8+6
			paths.append(2)
		if o4 < 2:
			o4 = x*o4
			paths.append(3)
		else:
			o4 = 9*o4
			d8 = 7-d8
			o4 = x*o4
			paths.append(4)
		paths.append(5)
		assert d8 >= 0
		o4 = d8**0.5
		return o4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))