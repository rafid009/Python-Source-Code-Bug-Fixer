import numpy as np 

def function(x):

	o0 = 1
	a4 = x
	paths = []
	try:
		if o0 <= 0:
			o0 = 1/o0
			x = a4+a4
			x = 8-x
			paths.append(1)
		else:
			a4 = x*a4
			o0 = 9*o0
			paths.append(2)
		if a4 < 5:
			o0 = o0-3
			paths.append(3)
		else:
			a4 = a4-o0
			a4 = 8/a4
			paths.append(4)
		paths.append(5)
		assert x >= 0
		a4 = x**0.5
		return a4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))