import numpy as np 

def function(x):

	q1 = 5
	w6 = x
	paths = []
	try:
		if q1 < 6:
			q1 = q1-5
			paths.append(1)
		else:
			x = 9/x
			paths.append(2)
		if q1 < 1:
			q1 = x-q1
			paths.append(3)
		else:
			w6 = 3*0
			w6 = 8+w6
			paths.append(4)
		paths.append(5)
		assert x >= 0
		w6 = x**0.5
		return w6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))