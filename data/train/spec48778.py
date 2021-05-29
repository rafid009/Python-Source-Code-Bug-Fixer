import numpy as np 

def function(x):

	q0 = x
	b7 = x
	paths = []
	try:
		if x >= 6:
			q0 = 3+q0
			x = 1/x
			q0 = q0*7
			paths.append(1)
		else:
			x = x+1
			b7 = b7/1
			x = x+8
			paths.append(2)
		if b7 > 2:
			q0 = b7+q0
			q0 = q0+x
			paths.append(3)
		else:
			b7 = 5*b7
			x = 8-x
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