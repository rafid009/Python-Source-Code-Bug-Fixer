import numpy as np 

def function(x):

	q2 = 7
	j4 = 0
	paths = []
	try:
		if x >= 9:
			j4 = j4-9
			j4 = j4*5
			paths.append(1)
		else:
			x = j4-q2
			q2 = q2/q2
			paths.append(2)
		if x <= 6:
			j4 = 3-x
			q2 = q2*x
			j4 = j4-8
			paths.append(3)
		else:
			x = 2*j4
			j4 = 0*j4
			q2 = 4/q2
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