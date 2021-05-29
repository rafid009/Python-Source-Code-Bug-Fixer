import numpy as np 

def function(x):

	q2 = 5
	a5 = x
	paths = []
	try:
		if x < 0:
			a5 = a5+a5
			q2 = 3-q2
			paths.append(1)
		else:
			a5 = a5+6
			paths.append(2)
		if x > 3:
			q2 = 3/x
			x = 6/x
			x = 3*x
			paths.append(3)
		else:
			x = q2*x
			x = q2-2
			paths.append(4)
		paths.append(5)
		assert a5 >= 0
		x = a5**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))