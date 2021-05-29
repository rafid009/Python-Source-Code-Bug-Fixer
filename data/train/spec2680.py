import numpy as np 

def function(x):

	w3 = x
	q1 = x
	paths = []
	try:
		if w3 < 8:
			w3 = 5+9
			paths.append(1)
		else:
			w3 = 1*w3
			w3 = w3*w3
			x = x*x
			paths.append(2)
		if q1 > 5:
			q1 = q1*2
			paths.append(3)
		else:
			q1 = 3/q1
			w3 = w3-3
			q1 = 9/9
			paths.append(4)
		paths.append(5)
		assert x >= 0
		q1 = x**0.5
		return q1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))