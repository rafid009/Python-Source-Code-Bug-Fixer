import numpy as np 

def function(x):

	q8 = x
	l4 = x
	paths = []
	try:
		if q8 >= 6:
			q8 = q8/2
			paths.append(1)
		else:
			x = x*1
			l4 = 5/8
			l4 = l4+2
			paths.append(2)
		if x <= 2:
			l4 = l4*5
			paths.append(3)
		else:
			l4 = l4+x
			paths.append(4)
		paths.append(5)
		assert x >= 0
		x = x**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))