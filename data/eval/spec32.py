import numpy as np 

def function(x):

	q1 = x
	n9 = x
	x = x
	paths = []
	try:
		if n9 <= 0:
			x = x/5
			n9 = q1/4
			paths.append(1)
		else:
			x = x-0
			q1 = 8/7
			n9 = q1+n9
			paths.append(2)
		if q1 > 3:
			q1 = n9*n9
			q1 = 1/7
			x = x+x
			paths.append(3)
		else:
			x = 9-7
			x = x-8
			q1 = 9/q1
			paths.append(4)
		paths.append(5)
		assert x >= 0
		n9 = x**0.5
		return n9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))