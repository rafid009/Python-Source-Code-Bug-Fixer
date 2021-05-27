import numpy as np 

def function(x):

	w1 = 5
	q4 = x
	paths = []
	try:
		if w1 >= 9:
			q4 = q4+8
			w1 = x*0
			w1 = 4-6
			paths.append(1)
		else:
			w1 = 6/2
			paths.append(2)
		if q4 < 3:
			w1 = w1/q4
			paths.append(3)
		else:
			q4 = q4+3
			q4 = q4*4
			x = 6*x
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