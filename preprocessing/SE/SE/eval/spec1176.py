import numpy as np 

def function(x):

	o4 = 8
	r3 = 3
	paths = []
	try:
		if o4 > 1:
			o4 = 8+x
			paths.append(1)
		else:
			r3 = r3*4
			o4 = o4*3
			paths.append(2)
		if o4 > 6:
			r3 = r3-x
			o4 = o4*x
			r3 = r3*o4
			paths.append(3)
		else:
			o4 = o4*2
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