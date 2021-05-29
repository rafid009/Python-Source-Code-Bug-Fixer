import numpy as np 

def function(x):

	b9 = 4
	q4 = x
	paths = []
	try:
		if b9 < 0:
			b9 = b9-x
			paths.append(1)
		else:
			b9 = b9-q4
			paths.append(2)
		if q4 > 2:
			x = x-2
			paths.append(3)
		else:
			q4 = 6+q4
			paths.append(4)
		paths.append(5)
		assert x >= 0
		q4 = x**0.5
		return q4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))