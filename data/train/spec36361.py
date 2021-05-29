import numpy as np 

def function(x):

	d0 = 9
	l7 = 1
	paths = []
	try:
		if d0 <= 2:
			l7 = l7/d0
			paths.append(1)
		else:
			x = d0+x
			d0 = d0-7
			paths.append(2)
		if x >= 1:
			x = x*4
			x = x+2
			paths.append(3)
		else:
			l7 = d0-l7
			d0 = 8/d0
			paths.append(4)
		paths.append(5)
		assert x >= 0
		l7 = x**0.5
		return l7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))