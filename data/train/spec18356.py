import numpy as np 

def function(x):

	l4 = x
	d7 = x
	x = x
	paths = []
	try:
		if l4 >= 1:
			l4 = l4+l4
			x = 6/x
			l4 = l4*d7
			paths.append(1)
		else:
			d7 = 4-l4
			paths.append(2)
		if l4 >= 5:
			x = x-l4
			x = d7*x
			x = 0*5
			paths.append(3)
		else:
			x = x*3
			l4 = 6+l4
			x = 6+x
			paths.append(4)
		paths.append(5)
		assert x >= 0
		l4 = x**0.5
		return l4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))