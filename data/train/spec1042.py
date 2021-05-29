import numpy as np 

def function(x):

	o0 = x
	l8 = x
	paths = []
	try:
		if x > 2:
			o0 = l8-2
			paths.append(1)
		else:
			l8 = x-9
			paths.append(2)
		if l8 <= 5:
			x = x-3
			l8 = l8-4
			x = 4*x
			paths.append(3)
		else:
			o0 = o0+o0
			x = x+0
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