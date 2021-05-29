import numpy as np 

def function(x):

	d7 = 9
	q7 = 8
	paths = []
	try:
		if d7 >= 9:
			d7 = 0-d7
			paths.append(1)
		else:
			d7 = d7+0
			q7 = x-5
			q7 = 0-8
			paths.append(2)
		if q7 > 7:
			q7 = 6-q7
			paths.append(3)
		else:
			d7 = 3/x
			paths.append(4)
		paths.append(5)
		assert q7 >= 0
		q7 = q7**0.5
		return q7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))