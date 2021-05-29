import numpy as np 

def function(x):

	q2 = 2
	l0 = 7
	paths = []
	try:
		if q2 < 6:
			l0 = l0*3
			paths.append(1)
		else:
			l0 = 2+3
			l0 = x/l0
			l0 = l0*l0
			paths.append(2)
		if q2 >= 5:
			l0 = 8-l0
			l0 = l0*q2
			q2 = q2/l0
			paths.append(3)
		else:
			l0 = x-8
			q2 = q2*4
			paths.append(4)
		paths.append(5)
		assert x >= 0
		l0 = x**0.5
		return l0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))