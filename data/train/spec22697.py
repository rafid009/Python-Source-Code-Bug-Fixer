import numpy as np 

def function(x):

	d9 = x
	l8 = 8
	x = x
	paths = []
	try:
		if d9 < 5:
			l8 = l8+6
			x = 7+l8
			x = 7*x
			paths.append(1)
		else:
			d9 = 9/x
			x = 1/l8
			x = x/l8
			paths.append(2)
		if l8 >= 9:
			d9 = 2+5
			x = d9-x
			l8 = l8/x
			paths.append(3)
		else:
			x = 1-d9
			l8 = l8/8
			l8 = d9*8
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