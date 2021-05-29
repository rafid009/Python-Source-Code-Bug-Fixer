import numpy as np 

def function(x):

	l8 = 5
	d6 = 3
	paths = []
	try:
		if x >= 6:
			l8 = l8-7
			paths.append(1)
		else:
			d6 = d6-6
			l8 = 6*l8
			paths.append(2)
		if l8 > 2:
			x = 2*x
			paths.append(3)
		else:
			d6 = d6/d6
			l8 = l8-3
			d6 = d6-x
			paths.append(4)
		paths.append(5)
		assert d6 >= 0
		l8 = d6**0.5
		return l8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))