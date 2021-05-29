import numpy as np 

def function(x):

	q7 = x
	o0 = 3
	paths = []
	try:
		if q7 < 9:
			x = o0-9
			o0 = 8+0
			q7 = o0-6
			paths.append(1)
		else:
			x = x-6
			q7 = 9-q7
			paths.append(2)
		if x >= 0:
			x = x-q7
			x = x+6
			paths.append(3)
		else:
			x = 2*x
			x = x-4
			o0 = 3/q7
			paths.append(4)
		paths.append(5)
		assert x >= 0
		q7 = x**0.5
		return q7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))