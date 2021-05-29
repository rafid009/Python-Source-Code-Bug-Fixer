import numpy as np 

def function(x):

	q5 = 4
	e4 = x
	paths = []
	try:
		if x > 0:
			x = 3-7
			q5 = q5-e4
			e4 = e4+3
			paths.append(1)
		else:
			x = 9*x
			q5 = 7+e4
			x = q5*q5
			paths.append(2)
		if q5 <= 3:
			q5 = q5-6
			paths.append(3)
		else:
			q5 = x+x
			e4 = e4*4
			paths.append(4)
		paths.append(5)
		assert x >= 0
		e4 = x**0.5
		return e4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))