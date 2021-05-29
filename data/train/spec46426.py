import numpy as np 

def function(x):

	q7 = 9
	w5 = 4
	paths = []
	try:
		if q7 < 1:
			q7 = q7/5
			paths.append(1)
		else:
			w5 = w5/x
			paths.append(2)
		if q7 >= 4:
			x = 0+w5
			paths.append(3)
		else:
			q7 = 6-q7
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