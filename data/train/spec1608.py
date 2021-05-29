import numpy as np 

def function(x):

	w1 = 9
	q7 = x
	paths = []
	try:
		if x < 9:
			w1 = w1/3
			w1 = 5-w1
			paths.append(1)
		else:
			w1 = w1-6
			paths.append(2)
		if w1 <= 5:
			q7 = 9*x
			w1 = w1/w1
			paths.append(3)
		else:
			q7 = q7/6
			paths.append(4)
		paths.append(5)
		assert x >= 0
		q7 = x**0.5
		return q7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))