import numpy as np 

def function(x):

	q0 = x
	l9 = x
	paths = []
	try:
		if l9 <= 5:
			x = x-3
			q0 = q0-1
			paths.append(1)
		else:
			q0 = q0/2
			x = x/3
			paths.append(2)
		if q0 <= 1:
			q0 = q0/3
			x = 4*x
			paths.append(3)
		else:
			x = 4*6
			x = x+l9
			q0 = q0-6
			paths.append(4)
		paths.append(5)
		assert x >= 0
		l9 = x**0.5
		return l9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))