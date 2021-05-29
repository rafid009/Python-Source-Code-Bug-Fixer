import numpy as np 

def function(x):

	l2 = x
	d0 = x
	paths = []
	try:
		if l2 >= 2:
			x = x-8
			l2 = l2/l2
			paths.append(1)
		else:
			d0 = d0+6
			x = d0+7
			paths.append(2)
		if x < 9:
			d0 = 9/d0
			l2 = l2/2
			l2 = d0*x
			paths.append(3)
		else:
			l2 = l2*l2
			l2 = l2*9
			paths.append(4)
		paths.append(5)
		assert d0 >= 0
		x = d0**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))