import numpy as np 

def function(x):

	v9 = 2
	q0 = 7
	paths = []
	try:
		if q0 >= 1:
			q0 = q0+q0
			paths.append(1)
		else:
			x = x*2
			x = 3/x
			paths.append(2)
		if q0 <= 8:
			q0 = 0+q0
			paths.append(3)
		else:
			x = x+q0
			paths.append(4)
		paths.append(5)
		assert x >= 0
		v9 = x**0.5
		return v9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))