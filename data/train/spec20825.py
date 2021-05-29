import numpy as np 

def function(x):

	l4 = 1
	r2 = x
	x = 4
	paths = []
	try:
		if x <= 0:
			x = 8/1
			paths.append(1)
		else:
			l4 = 1/l4
			x = 8*x
			paths.append(2)
		if r2 < 3:
			l4 = l4/1
			paths.append(3)
		else:
			l4 = l4-2
			paths.append(4)
		paths.append(5)
		assert l4 >= 0
		l4 = l4**0.5
		return l4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))