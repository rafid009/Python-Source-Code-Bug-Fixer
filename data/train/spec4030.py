import numpy as np 

def function(x):

	a6 = 7
	q2 = x
	paths = []
	try:
		if q2 <= 4:
			a6 = a6*3
			a6 = a6/1
			paths.append(1)
		else:
			q2 = q2*5
			paths.append(2)
		if x < 0:
			q2 = x-1
			q2 = q2+a6
			paths.append(3)
		else:
			a6 = 8+a6
			x = 0-9
			paths.append(4)
		paths.append(5)
		assert x >= 0
		a6 = x**0.5
		return a6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))