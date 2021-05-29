import numpy as np 

def function(x):

	o6 = x
	q1 = 8
	paths = []
	try:
		if q1 <= 6:
			o6 = o6/q1
			x = x+5
			paths.append(1)
		else:
			q1 = 3-q1
			paths.append(2)
		if o6 >= 6:
			q1 = 6/x
			x = x/q1
			o6 = o6-4
			paths.append(3)
		else:
			x = x*q1
			q1 = 6+0
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