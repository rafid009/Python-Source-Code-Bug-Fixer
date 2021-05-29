import numpy as np 

def function(x):

	q9 = x
	e6 = 4
	paths = []
	try:
		if q9 < 3:
			q9 = q9+e6
			paths.append(1)
		else:
			e6 = 2/1
			e6 = e6-8
			paths.append(2)
		if e6 >= 1:
			q9 = 7/q9
			q9 = q9+q9
			paths.append(3)
		else:
			x = x/e6
			x = x/e6
			paths.append(4)
		paths.append(5)
		assert x >= 0
		e6 = x**0.5
		return e6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))