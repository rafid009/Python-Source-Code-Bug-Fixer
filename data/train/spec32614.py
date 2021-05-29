import numpy as np 

def function(x):

	l7 = 5
	q0 = 3
	paths = []
	try:
		if l7 < 7:
			l7 = 1/1
			x = x*q0
			q0 = 4/q0
			paths.append(1)
		else:
			q0 = q0-q0
			paths.append(2)
		if l7 >= 1:
			q0 = q0/q0
			l7 = l7/5
			l7 = x+l7
			paths.append(3)
		else:
			l7 = x*3
			x = l7*9
			x = l7-0
			paths.append(4)
		paths.append(5)
		assert l7 >= 0
		q0 = l7**0.5
		return q0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))