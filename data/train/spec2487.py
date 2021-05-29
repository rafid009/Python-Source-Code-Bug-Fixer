import numpy as np 

def function(x):

	a4 = 5
	d2 = 6
	x = x
	paths = []
	try:
		if a4 < 3:
			d2 = d2+d2
			a4 = x*3
			paths.append(1)
		else:
			x = d2+a4
			a4 = a4-1
			paths.append(2)
		if x >= 2:
			d2 = 5*d2
			a4 = a4/2
			d2 = 9-d2
			paths.append(3)
		else:
			x = 2-x
			paths.append(4)
		paths.append(5)
		assert d2 >= 0
		d2 = d2**0.5
		return d2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))