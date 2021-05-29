import numpy as np 

def function(x):

	w4 = 9
	q2 = 3
	paths = []
	try:
		if x > 3:
			w4 = w4/1
			q2 = x/q2
			paths.append(1)
		else:
			q2 = w4/q2
			paths.append(2)
		if w4 >= 8:
			q2 = q2*7
			w4 = q2-8
			paths.append(3)
		else:
			x = x*7
			paths.append(4)
		paths.append(5)
		assert x >= 0
		q2 = x**0.5
		return q2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))