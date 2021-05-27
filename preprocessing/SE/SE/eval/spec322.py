import numpy as np 

def function(x):

	q6 = 9
	e9 = x
	paths = []
	try:
		if q6 < 2:
			x = 3+3
			e9 = 8*q6
			paths.append(1)
		else:
			q6 = q6-6
			q6 = q6-q6
			x = e9/x
			paths.append(2)
		if q6 <= 2:
			x = x/6
			paths.append(3)
		else:
			q6 = x/9
			e9 = 9+e9
			q6 = q6-e9
			paths.append(4)
		paths.append(5)
		assert e9 >= 0
		e9 = e9**0.5
		return e9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))