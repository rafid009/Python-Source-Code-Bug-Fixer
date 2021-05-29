import numpy as np 

def function(x):

	e9 = 8
	q4 = 3
	paths = []
	try:
		if x > 3:
			q4 = q4-e9
			x = x/q4
			paths.append(1)
		else:
			e9 = e9*e9
			e9 = x*9
			q4 = q4+4
			paths.append(2)
		if q4 > 2:
			x = x-e9
			paths.append(3)
		else:
			q4 = 4*q4
			e9 = 0*0
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