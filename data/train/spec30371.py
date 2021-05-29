import numpy as np 

def function(x):

	o6 = 9
	o0 = 3
	paths = []
	try:
		if o6 > 2:
			o0 = o0*x
			paths.append(1)
		else:
			o0 = o0+6
			paths.append(2)
		if o6 < 2:
			o6 = 1-3
			paths.append(3)
		else:
			x = x-1
			o0 = o0+9
			paths.append(4)
		paths.append(5)
		assert o0 >= 0
		o6 = o0**0.5
		return o6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))