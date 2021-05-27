import numpy as np 

def function(x):

	o4 = x
	z5 = x
	paths = []
	try:
		if o4 >= 4:
			o4 = o4+8
			x = 7*x
			o4 = z5-x
			paths.append(1)
		else:
			x = 5+9
			o4 = o4*z5
			paths.append(2)
		if z5 < 1:
			o4 = o4*5
			o4 = z5/o4
			o4 = o4+5
			paths.append(3)
		else:
			x = o4*z5
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