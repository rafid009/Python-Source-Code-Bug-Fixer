import numpy as np 

def function(x):

	q0 = x
	a6 = x
	paths = []
	try:
		if x <= 7:
			a6 = 8+2
			a6 = a6/7
			paths.append(1)
		else:
			a6 = a6-a6
			a6 = 2-1
			q0 = q0+q0
			paths.append(2)
		if q0 < 2:
			a6 = 5+a6
			paths.append(3)
		else:
			a6 = 1*a6
			q0 = q0/q0
			paths.append(4)
		paths.append(5)
		assert x >= 0
		q0 = x**0.5
		return q0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))