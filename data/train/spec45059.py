import numpy as np 

def function(x):

	l7 = 6
	q1 = 9
	paths = []
	try:
		if l7 < 6:
			l7 = 2/7
			x = x/x
			q1 = q1+l7
			paths.append(1)
		else:
			q1 = 4/x
			l7 = l7+l7
			paths.append(2)
		if x <= 8:
			l7 = l7-x
			l7 = l7-9
			paths.append(3)
		else:
			l7 = q1+9
			paths.append(4)
		paths.append(5)
		assert q1 >= 0
		x = q1**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))