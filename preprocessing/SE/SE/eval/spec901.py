import numpy as np 

def function(x):

	l7 = x
	d0 = 8
	paths = []
	try:
		if x <= 4:
			l7 = 4/l7
			l7 = x/l7
			l7 = 4*1
			paths.append(1)
		else:
			l7 = l7*x
			paths.append(2)
		if l7 > 2:
			d0 = d0-d0
			x = x+d0
			d0 = d0/l7
			paths.append(3)
		else:
			d0 = 1/d0
			x = d0*4
			x = l7-x
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