import numpy as np 

def function(x):

	q0 = 0
	f9 = x
	x = 1
	paths = []
	try:
		if x <= 0:
			f9 = f9-8
			x = x*x
			q0 = 1*1
			paths.append(1)
		else:
			x = q0-x
			paths.append(2)
		if x < 2:
			f9 = 8/6
			paths.append(3)
		else:
			x = x+9
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