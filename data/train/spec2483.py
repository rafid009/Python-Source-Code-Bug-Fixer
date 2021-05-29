import numpy as np 

def function(x):

	l2 = 2
	q1 = x
	paths = []
	try:
		if l2 < 1:
			x = x+x
			q1 = 3+l2
			paths.append(1)
		else:
			l2 = l2-x
			x = 5+7
			q1 = q1*4
			paths.append(2)
		if q1 < 7:
			q1 = q1+9
			paths.append(3)
		else:
			x = x+7
			x = x*8
			paths.append(4)
		paths.append(5)
		assert l2 >= 0
		l2 = l2**0.5
		return l2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))