import numpy as np 

def function(x):

	q9 = 7
	l4 = x
	paths = []
	try:
		if q9 >= 3:
			x = x*x
			paths.append(1)
		else:
			l4 = l4+l4
			l4 = 9+8
			q9 = q9*9
			paths.append(2)
		if x >= 7:
			l4 = q9/q9
			x = 6/x
			l4 = l4+8
			paths.append(3)
		else:
			q9 = 7/l4
			l4 = q9/l4
			paths.append(4)
		paths.append(5)
		assert q9 >= 0
		x = q9**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))