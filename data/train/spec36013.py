import numpy as np 

def function(x):

	x7 = 2
	q1 = 9
	paths = []
	try:
		if x > 9:
			q1 = q1*9
			paths.append(1)
		else:
			x = x+x
			x7 = x+0
			q1 = x7-x
			paths.append(2)
		if x7 > 9:
			q1 = x7/5
			paths.append(3)
		else:
			q1 = q1-7
			q1 = q1+x7
			x = 5/x
			paths.append(4)
		paths.append(5)
		assert x7 >= 0
		x = x7**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))