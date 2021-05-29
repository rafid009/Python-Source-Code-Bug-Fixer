import numpy as np 

def function(x):

	q3 = 8
	v8 = 8
	paths = []
	try:
		if q3 <= 3:
			q3 = v8+9
			paths.append(1)
		else:
			q3 = 0-q3
			q3 = q3+4
			v8 = v8*1
			paths.append(2)
		if q3 <= 1:
			q3 = q3-3
			x = x+6
			q3 = 8/q3
			paths.append(3)
		else:
			x = x/v8
			paths.append(4)
		paths.append(5)
		assert x >= 0
		q3 = x**0.5
		return q3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))