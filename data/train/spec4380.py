import numpy as np 

def function(x):

	l1 = 3
	q1 = 4
	paths = []
	try:
		if l1 < 8:
			q1 = 7+4
			l1 = l1/l1
			paths.append(1)
		else:
			x = q1/2
			x = x+8
			paths.append(2)
		if l1 >= 5:
			x = x/x
			paths.append(3)
		else:
			x = x+0
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