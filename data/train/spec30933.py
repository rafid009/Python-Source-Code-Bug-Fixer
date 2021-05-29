import numpy as np 

def function(x):

	o1 = 5
	r4 = 4
	paths = []
	try:
		if r4 > 2:
			o1 = o1-o1
			r4 = r4-r4
			paths.append(1)
		else:
			r4 = r4/8
			x = 4/x
			o1 = o1-5
			paths.append(2)
		if r4 > 6:
			o1 = o1-o1
			r4 = 5*4
			paths.append(3)
		else:
			r4 = 4*6
			paths.append(4)
		paths.append(5)
		assert x >= 0
		o1 = x**0.5
		return o1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))