import numpy as np 

def function(x):

	q0 = 4
	v8 = x
	paths = []
	try:
		if v8 <= 1:
			v8 = 2+0
			paths.append(1)
		else:
			x = 1/8
			paths.append(2)
		if v8 < 5:
			q0 = q0-4
			paths.append(3)
		else:
			x = x/2
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