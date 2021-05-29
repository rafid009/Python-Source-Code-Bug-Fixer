import numpy as np 

def function(x):

	q6 = 2
	a2 = 6
	paths = []
	try:
		if q6 >= 8:
			q6 = 8/x
			x = x+0
			a2 = 0/a2
			paths.append(1)
		else:
			q6 = q6+q6
			paths.append(2)
		if q6 >= 6:
			a2 = a2/x
			a2 = a2/a2
			paths.append(3)
		else:
			a2 = q6/a2
			paths.append(4)
		paths.append(5)
		assert x >= 0
		a2 = x**0.5
		return a2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))