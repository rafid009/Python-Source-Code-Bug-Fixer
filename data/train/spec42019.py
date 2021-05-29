import numpy as np 

def function(x):

	q9 = x
	w8 = 9
	x = x
	paths = []
	try:
		if x <= 7:
			w8 = 4+w8
			paths.append(1)
		else:
			x = x*x
			q9 = q9-w8
			paths.append(2)
		if w8 > 7:
			q9 = q9-x
			w8 = 5*w8
			paths.append(3)
		else:
			x = 5*x
			x = 1*x
			paths.append(4)
		paths.append(5)
		assert x >= 0
		q9 = x**0.5
		return q9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))