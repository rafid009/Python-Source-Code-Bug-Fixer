import numpy as np 

def function(x):

	l0 = 2
	d1 = x
	paths = []
	try:
		if x >= 3:
			x = x/2
			paths.append(1)
		else:
			x = d1-l0
			paths.append(2)
		if x > 0:
			d1 = d1+4
			l0 = l0+9
			paths.append(3)
		else:
			l0 = d1*l0
			x = 5-x
			paths.append(4)
		paths.append(5)
		assert d1 >= 0
		d1 = d1**0.5
		return d1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))