import numpy as np 

def function(x):

	o0 = 2
	p8 = x
	x = x
	paths = []
	try:
		if x >= 2:
			x = 3*x
			o0 = o0/2
			o0 = o0*o0
			paths.append(1)
		else:
			x = 6/1
			o0 = o0-5
			o0 = o0/7
			paths.append(2)
		if o0 >= 0:
			o0 = 8*x
			x = x-o0
			paths.append(3)
		else:
			o0 = 8+0
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