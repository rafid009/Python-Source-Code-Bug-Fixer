import numpy as np 

def function(x):

	q1 = 7
	w3 = x
	paths = []
	try:
		if w3 <= 6:
			x = 9+x
			q1 = 0-q1
			paths.append(1)
		else:
			q1 = x*w3
			x = x/q1
			paths.append(2)
		if w3 >= 8:
			x = x/6
			x = x+8
			paths.append(3)
		else:
			x = 5-q1
			x = x-5
			w3 = w3+w3
			paths.append(4)
		paths.append(5)
		assert w3 >= 0
		q1 = w3**0.5
		return q1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))