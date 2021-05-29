import numpy as np 

def function(x):

	l7 = 7
	x4 = 7
	paths = []
	try:
		if x <= 6:
			l7 = l7/4
			x = x/4
			l7 = 4-x4
			paths.append(1)
		else:
			x4 = x4*5
			x = 2*x
			x4 = 8+x4
			paths.append(2)
		if x <= 4:
			x4 = x4/l7
			paths.append(3)
		else:
			l7 = l7-5
			x4 = 6-x4
			x = l7*x
			paths.append(4)
		paths.append(5)
		assert l7 >= 0
		x = l7**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))