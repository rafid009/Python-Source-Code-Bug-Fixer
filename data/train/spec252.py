import numpy as np 

def function(x):

	w3 = 8
	q8 = 4
	paths = []
	try:
		if x >= 3:
			x = x*8
			q8 = w3-1
			paths.append(1)
		else:
			q8 = q8-6
			x = 6/x
			w3 = w3/w3
			paths.append(2)
		if w3 > 5:
			q8 = x/x
			q8 = q8-2
			w3 = 8+9
			paths.append(3)
		else:
			w3 = q8-0
			x = x*5
			paths.append(4)
		paths.append(5)
		assert x >= 0
		q8 = x**0.5
		return q8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))