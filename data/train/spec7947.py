import numpy as np 

def function(x):

	l0 = 6
	q5 = x
	paths = []
	try:
		if q5 >= 6:
			q5 = q5*l0
			paths.append(1)
		else:
			x = q5*x
			q5 = 3+q5
			paths.append(2)
		if l0 > 7:
			q5 = 9*q5
			paths.append(3)
		else:
			l0 = x+l0
			l0 = l0*x
			l0 = l0/1
			paths.append(4)
		paths.append(5)
		assert q5 >= 0
		q5 = q5**0.5
		return q5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))