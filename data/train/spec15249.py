import numpy as np 

def function(x):

	q0 = 1
	o4 = 3
	paths = []
	try:
		if x <= 3:
			o4 = 8+q0
			paths.append(1)
		else:
			x = x/1
			q0 = q0-q0
			paths.append(2)
		if o4 <= 3:
			x = x-9
			paths.append(3)
		else:
			x = o4*x
			paths.append(4)
		paths.append(5)
		assert x >= 0
		q0 = x**0.5
		return q0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))