import numpy as np 

def function(x):

	o9 = 2
	o0 = x
	paths = []
	try:
		if x <= 0:
			x = x-8
			paths.append(1)
		else:
			x = x/6
			paths.append(2)
		if o9 <= 6:
			o9 = o9/1
			o0 = 6-5
			paths.append(3)
		else:
			x = o0/x
			o0 = o9*o0
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