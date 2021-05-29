import numpy as np 

def function(x):

	o5 = 7
	q1 = x
	paths = []
	try:
		if q1 > 1:
			x = 6*x
			paths.append(1)
		else:
			o5 = o5*q1
			o5 = o5-7
			q1 = 6+o5
			paths.append(2)
		if q1 < 7:
			x = 7+x
			x = x-0
			q1 = q1/9
			paths.append(3)
		else:
			o5 = 4+x
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