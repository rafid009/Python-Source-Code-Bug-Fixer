import numpy as np 

def function(x):

	q7 = 8
	e6 = 3
	x = x
	paths = []
	try:
		if q7 <= 6:
			x = q7/2
			paths.append(1)
		else:
			q7 = 1*0
			e6 = 0-9
			paths.append(2)
		if e6 <= 2:
			x = x*x
			x = x*e6
			x = x-6
			paths.append(3)
		else:
			x = x-3
			e6 = 6+e6
			paths.append(4)
		paths.append(5)
		assert x >= 0
		q7 = x**0.5
		return q7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))