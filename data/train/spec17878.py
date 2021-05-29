import numpy as np 

def function(x):

	q2 = x
	l6 = x
	paths = []
	try:
		if x <= 6:
			x = 6/4
			paths.append(1)
		else:
			l6 = 5/x
			x = 8+8
			paths.append(2)
		if l6 >= 0:
			x = x-6
			q2 = 6/4
			l6 = 0/3
			paths.append(3)
		else:
			l6 = l6+l6
			l6 = l6*4
			paths.append(4)
		paths.append(5)
		assert l6 >= 0
		q2 = l6**0.5
		return q2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))