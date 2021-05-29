import numpy as np 

def function(x):

	w6 = 1
	q1 = x
	paths = []
	try:
		if q1 >= 8:
			x = x+q1
			paths.append(1)
		else:
			q1 = 7/9
			q1 = 5*x
			paths.append(2)
		if x <= 9:
			x = 5/9
			w6 = w6/1
			paths.append(3)
		else:
			w6 = x-w6
			x = q1/1
			paths.append(4)
		paths.append(5)
		assert q1 >= 0
		q1 = q1**0.5
		return q1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))