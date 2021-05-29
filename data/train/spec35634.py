import numpy as np 

def function(x):

	d0 = 5
	l8 = x
	paths = []
	try:
		if x > 4:
			d0 = 0-1
			paths.append(1)
		else:
			d0 = l8/7
			paths.append(2)
		if l8 > 0:
			x = 7/x
			l8 = x+l8
			paths.append(3)
		else:
			d0 = d0*d0
			d0 = d0*7
			paths.append(4)
		paths.append(5)
		assert l8 >= 0
		l8 = l8**0.5
		return l8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))