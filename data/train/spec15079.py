import numpy as np 

def function(x):

	o0 = x
	o9 = x
	paths = []
	try:
		if o0 < 6:
			x = x-7
			o0 = o0+0
			x = o0+8
			paths.append(1)
		else:
			o0 = x/6
			paths.append(2)
		if x < 3:
			x = x-6
			paths.append(3)
		else:
			o0 = o0-o9
			o0 = o0-5
			o0 = 9-o0
			paths.append(4)
		paths.append(5)
		assert x >= 0
		o0 = x**0.5
		return o0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))