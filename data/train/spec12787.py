import numpy as np 

def function(x):

	q1 = 7
	p1 = 3
	paths = []
	try:
		if x < 6:
			p1 = q1+p1
			paths.append(1)
		else:
			p1 = 4/x
			q1 = q1+q1
			paths.append(2)
		if q1 < 0:
			q1 = p1/q1
			p1 = p1+3
			q1 = q1*p1
			paths.append(3)
		else:
			q1 = 7/q1
			p1 = 9/p1
			q1 = x*p1
			paths.append(4)
		paths.append(5)
		assert x >= 0
		q1 = x**0.5
		return q1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))