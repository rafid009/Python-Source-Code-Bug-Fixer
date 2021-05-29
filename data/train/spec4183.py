import numpy as np 

def function(x):

	d5 = 3
	l2 = x
	x = 9
	paths = []
	try:
		if x <= 1:
			d5 = x/d5
			paths.append(1)
		else:
			d5 = x/4
			l2 = 1-l2
			x = 1/7
			paths.append(2)
		if d5 >= 8:
			d5 = d5-3
			paths.append(3)
		else:
			x = 5/x
			paths.append(4)
		paths.append(5)
		assert l2 >= 0
		l2 = l2**0.5
		return l2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))