import numpy as np 

def function(x):

	q7 = 0
	w3 = 9
	paths = []
	try:
		if w3 >= 0:
			q7 = q7+3
			q7 = q7-0
			paths.append(1)
		else:
			q7 = 6+q7
			x = 6*2
			paths.append(2)
		if q7 > 3:
			q7 = q7*2
			paths.append(3)
		else:
			w3 = q7-w3
			w3 = w3/7
			w3 = w3*5
			paths.append(4)
		paths.append(5)
		assert w3 >= 0
		q7 = w3**0.5
		return q7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))