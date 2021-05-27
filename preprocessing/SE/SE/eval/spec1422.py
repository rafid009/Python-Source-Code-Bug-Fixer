import numpy as np 

def function(x):

	q0 = 2
	h3 = 4
	paths = []
	try:
		if q0 >= 7:
			q0 = 6*9
			h3 = x*h3
			paths.append(1)
		else:
			q0 = 5+q0
			paths.append(2)
		if q0 <= 1:
			q0 = 1+h3
			h3 = h3/8
			paths.append(3)
		else:
			x = x*7
			q0 = 5*8
			x = x-3
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