import numpy as np 

def function(x):

	q1 = 0
	n6 = 7
	paths = []
	try:
		if x > 1:
			n6 = n6/x
			q1 = 3+q1
			x = 4+q1
			paths.append(1)
		else:
			n6 = n6+n6
			n6 = 1-n6
			paths.append(2)
		if n6 >= 4:
			x = n6-q1
			paths.append(3)
		else:
			x = x-1
			q1 = q1-n6
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