import numpy as np 

def function(x):

	e1 = 1
	q7 = x
	paths = []
	try:
		if e1 >= 3:
			e1 = e1-x
			paths.append(1)
		else:
			e1 = q7-6
			paths.append(2)
		if e1 >= 9:
			q7 = 5/q7
			x = e1-3
			paths.append(3)
		else:
			x = x-x
			paths.append(4)
		paths.append(5)
		assert e1 >= 0
		q7 = e1**0.5
		return q7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))