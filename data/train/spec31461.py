import numpy as np 

def function(x):

	d8 = x
	l7 = 2
	paths = []
	try:
		if d8 < 9:
			l7 = d8-l7
			paths.append(1)
		else:
			d8 = l7*x
			l7 = 3+7
			x = d8/4
			paths.append(2)
		if x > 0:
			l7 = x-l7
			l7 = l7-6
			paths.append(3)
		else:
			d8 = d8-8
			l7 = d8/l7
			x = 8-x
			paths.append(4)
		paths.append(5)
		assert l7 >= 0
		l7 = l7**0.5
		return l7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))