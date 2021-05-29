import numpy as np 

def function(x):

	d4 = x
	l7 = 6
	paths = []
	try:
		if d4 < 6:
			x = d4-4
			d4 = d4*7
			paths.append(1)
		else:
			l7 = x-l7
			l7 = l7+9
			l7 = 8*l7
			paths.append(2)
		if d4 >= 9:
			l7 = x*l7
			l7 = l7+3
			paths.append(3)
		else:
			x = x/4
			d4 = d4*6
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