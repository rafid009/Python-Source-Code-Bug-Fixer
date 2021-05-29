import numpy as np 

def function(x):

	q1 = 9
	o5 = 5
	paths = []
	try:
		if q1 < 0:
			o5 = o5-4
			paths.append(1)
		else:
			q1 = q1-1
			x = 3-x
			paths.append(2)
		if o5 <= 2:
			o5 = 3/o5
			x = o5-x
			paths.append(3)
		else:
			x = x-1
			x = o5-x
			paths.append(4)
		paths.append(5)
		assert x >= 0
		o5 = x**0.5
		return o5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))