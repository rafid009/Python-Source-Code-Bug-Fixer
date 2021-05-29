import numpy as np 

def function(x):

	l6 = x
	q6 = 8
	paths = []
	try:
		if q6 < 4:
			x = 1+6
			q6 = 4+q6
			paths.append(1)
		else:
			x = x-6
			l6 = 7+l6
			x = 2-x
			paths.append(2)
		if x <= 8:
			x = x+q6
			x = x*q6
			l6 = 5/l6
			paths.append(3)
		else:
			x = 1*q6
			paths.append(4)
		paths.append(5)
		assert l6 >= 0
		l6 = l6**0.5
		return l6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))