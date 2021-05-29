import numpy as np 

def function(x):

	r8 = x
	o4 = x
	paths = []
	try:
		if o4 > 8:
			o4 = 4-o4
			o4 = 9*r8
			paths.append(1)
		else:
			r8 = r8-5
			o4 = r8-o4
			o4 = 6*7
			paths.append(2)
		if o4 <= 8:
			x = o4-x
			paths.append(3)
		else:
			o4 = 6/o4
			o4 = x-0
			paths.append(4)
		paths.append(5)
		assert x >= 0
		r8 = x**0.5
		return r8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))