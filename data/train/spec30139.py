import numpy as np 

def function(x):

	l4 = 3
	q2 = x
	paths = []
	try:
		if q2 > 5:
			q2 = q2+9
			x = 3+x
			paths.append(1)
		else:
			q2 = 5*q2
			q2 = 2+q2
			q2 = 6/q2
			paths.append(2)
		if q2 >= 9:
			q2 = 5*q2
			l4 = l4*3
			x = x-l4
			paths.append(3)
		else:
			q2 = 2*x
			l4 = 0*l4
			x = q2*q2
			paths.append(4)
		paths.append(5)
		assert x >= 0
		q2 = x**0.5
		return q2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))