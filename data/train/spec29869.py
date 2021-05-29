import numpy as np 

def function(x):

	q8 = 7
	e7 = 7
	paths = []
	try:
		if x < 7:
			q8 = 0-q8
			e7 = e7-e7
			x = e7+6
			paths.append(1)
		else:
			x = 7/x
			q8 = q8+q8
			paths.append(2)
		if x < 4:
			e7 = 2/x
			paths.append(3)
		else:
			x = 4/2
			q8 = q8-6
			e7 = e7-7
			paths.append(4)
		paths.append(5)
		assert q8 >= 0
		e7 = q8**0.5
		return e7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))