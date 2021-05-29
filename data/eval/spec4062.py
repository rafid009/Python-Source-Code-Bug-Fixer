import numpy as np 

def function(x):

	q5 = x
	w3 = x
	x = 5
	paths = []
	try:
		if w3 > 7:
			x = 5-6
			w3 = 4/w3
			q5 = q5+q5
			paths.append(1)
		else:
			w3 = 1-w3
			q5 = 9-5
			paths.append(2)
		if w3 < 3:
			x = x-8
			w3 = w3-1
			paths.append(3)
		else:
			w3 = w3*6
			w3 = 1-w3
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