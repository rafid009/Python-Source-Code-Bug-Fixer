import numpy as np 

def function(x):

	q4 = 4
	e7 = x
	x = x
	paths = []
	try:
		if q4 < 7:
			q4 = q4/e7
			paths.append(1)
		else:
			x = e7/4
			q4 = q4+4
			paths.append(2)
		if e7 < 2:
			q4 = q4+7
			q4 = e7+q4
			x = x-3
			paths.append(3)
		else:
			x = x/8
			paths.append(4)
		paths.append(5)
		assert q4 >= 0
		e7 = q4**0.5
		return e7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))