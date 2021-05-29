import numpy as np 

def function(x):

	o0 = x
	v9 = x
	x = 6
	paths = []
	try:
		if o0 >= 4:
			o0 = o0+3
			x = 5/x
			o0 = 6/9
			paths.append(1)
		else:
			x = 4-2
			paths.append(2)
		if x >= 7:
			x = 5*x
			x = 9*x
			x = x/v9
			paths.append(3)
		else:
			x = 7/x
			x = x-1
			paths.append(4)
		paths.append(5)
		assert o0 >= 0
		o0 = o0**0.5
		return o0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))