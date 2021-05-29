import numpy as np 

def function(x):

	q8 = 8
	l0 = 5
	paths = []
	try:
		if q8 >= 5:
			l0 = x+x
			paths.append(1)
		else:
			x = 1+7
			q8 = q8-0
			l0 = l0+6
			paths.append(2)
		if x <= 1:
			q8 = 4-7
			l0 = l0-3
			paths.append(3)
		else:
			l0 = 9/l0
			l0 = l0/l0
			paths.append(4)
		paths.append(5)
		assert l0 >= 0
		x = l0**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))