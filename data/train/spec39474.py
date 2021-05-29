import numpy as np 

def function(x):

	q8 = 3
	w7 = x
	x = x
	paths = []
	try:
		if x <= 8:
			q8 = x+q8
			q8 = 3-q8
			paths.append(1)
		else:
			x = w7*4
			q8 = q8*q8
			paths.append(2)
		if x < 5:
			w7 = q8*w7
			paths.append(3)
		else:
			q8 = q8/5
			paths.append(4)
		paths.append(5)
		assert w7 >= 0
		q8 = w7**0.5
		return q8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))