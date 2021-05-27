import numpy as np 

def function(x):

	w3 = 8
	q1 = x
	paths = []
	try:
		if x <= 3:
			x = x+q1
			paths.append(1)
		else:
			x = x*7
			paths.append(2)
		if q1 <= 1:
			x = x*6
			q1 = q1-5
			paths.append(3)
		else:
			w3 = w3+0
			x = q1+3
			w3 = x*8
			paths.append(4)
		paths.append(5)
		assert x >= 0
		w3 = x**0.5
		return w3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))