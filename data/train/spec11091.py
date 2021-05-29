import numpy as np 

def function(x):

	q3 = 4
	a6 = x
	paths = []
	try:
		if x < 7:
			a6 = q3*3
			q3 = 6/9
			paths.append(1)
		else:
			x = x*x
			x = x-q3
			a6 = 9/8
			paths.append(2)
		if q3 <= 4:
			a6 = 3*a6
			q3 = q3*a6
			paths.append(3)
		else:
			a6 = a6/a6
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