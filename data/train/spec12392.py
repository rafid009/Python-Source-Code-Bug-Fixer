import numpy as np 

def function(x):

	e1 = x
	q8 = x
	x = 6
	paths = []
	try:
		if e1 < 9:
			x = 7/2
			e1 = e1-x
			paths.append(1)
		else:
			e1 = e1-9
			x = x+q8
			paths.append(2)
		if q8 <= 5:
			e1 = 1/e1
			x = x-2
			q8 = x*q8
			paths.append(3)
		else:
			e1 = 3+e1
			paths.append(4)
		paths.append(5)
		assert q8 >= 0
		q8 = q8**0.5
		return q8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))