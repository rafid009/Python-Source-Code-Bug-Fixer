import numpy as np 

def function(x):

	a7 = 9
	d1 = 3
	paths = []
	try:
		if d1 < 1:
			a7 = 1+a7
			a7 = a7-2
			paths.append(1)
		else:
			x = 6/d1
			d1 = d1/d1
			d1 = d1-a7
			paths.append(2)
		if d1 >= 1:
			x = x/6
			d1 = d1+a7
			a7 = d1/8
			paths.append(3)
		else:
			d1 = 2/d1
			x = 9+3
			x = 5*x
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