import numpy as np 

def function(x):

	j9 = x
	q0 = 9
	paths = []
	try:
		if x <= 8:
			j9 = q0/j9
			x = x/1
			q0 = 3+j9
			paths.append(1)
		else:
			x = x/x
			q0 = x-q0
			paths.append(2)
		if j9 <= 5:
			q0 = 4-9
			paths.append(3)
		else:
			x = 2-x
			x = x-j9
			q0 = 7*q0
			paths.append(4)
		paths.append(5)
		assert x >= 0
		x = x**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))