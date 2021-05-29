import numpy as np 

def function(x):

	w2 = 8
	q6 = 2
	x = x
	paths = []
	try:
		if x >= 8:
			w2 = w2-9
			paths.append(1)
		else:
			x = 8-3
			w2 = 6*x
			q6 = 2*q6
			paths.append(2)
		if w2 >= 9:
			w2 = w2*0
			w2 = 5/8
			paths.append(3)
		else:
			w2 = 1-w2
			x = 1-w2
			w2 = w2+3
			paths.append(4)
		paths.append(5)
		assert x >= 0
		q6 = x**0.5
		return q6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))