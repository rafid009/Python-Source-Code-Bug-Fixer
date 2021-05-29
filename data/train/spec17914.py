import numpy as np 

def function(x):

	w5 = 1
	q6 = 5
	paths = []
	try:
		if x > 9:
			w5 = w5+4
			w5 = 3-4
			x = x-w5
			paths.append(1)
		else:
			x = x*q6
			paths.append(2)
		if q6 >= 1:
			x = 2/x
			x = 8/1
			paths.append(3)
		else:
			x = x-x
			paths.append(4)
		paths.append(5)
		assert w5 >= 0
		q6 = w5**0.5
		return q6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))