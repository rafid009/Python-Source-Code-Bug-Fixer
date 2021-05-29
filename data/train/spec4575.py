import numpy as np 

def function(x):

	o9 = 2
	q9 = 6
	paths = []
	try:
		if q9 <= 6:
			o9 = 2/x
			paths.append(1)
		else:
			o9 = o9/o9
			x = x+o9
			paths.append(2)
		if q9 >= 1:
			q9 = x/x
			q9 = o9*8
			paths.append(3)
		else:
			q9 = q9-4
			paths.append(4)
		paths.append(5)
		assert x >= 0
		q9 = x**0.5
		return q9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))