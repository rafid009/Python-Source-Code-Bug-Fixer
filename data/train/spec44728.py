import numpy as np 

def function(x):

	l6 = 5
	r9 = x
	paths = []
	try:
		if x > 6:
			x = x*x
			r9 = r9*r9
			paths.append(1)
		else:
			r9 = r9/6
			paths.append(2)
		if x >= 2:
			l6 = r9/9
			l6 = 6-8
			paths.append(3)
		else:
			l6 = l6-r9
			x = 0+8
			r9 = 8-3
			paths.append(4)
		paths.append(5)
		assert l6 >= 0
		x = l6**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))