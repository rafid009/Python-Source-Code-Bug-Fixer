import numpy as np 

def function(x):

	w3 = 6
	q1 = x
	x = x
	paths = []
	try:
		if q1 < 7:
			w3 = w3+8
			q1 = q1+7
			paths.append(1)
		else:
			w3 = 2+w3
			w3 = 6/w3
			paths.append(2)
		if w3 >= 9:
			w3 = 0-q1
			q1 = w3/q1
			paths.append(3)
		else:
			w3 = 7-6
			paths.append(4)
		paths.append(5)
		assert w3 >= 0
		x = w3**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))