import numpy as np 

def function(x):

	a2 = 7
	d0 = 9
	x = x
	paths = []
	try:
		if a2 > 5:
			d0 = 7-d0
			a2 = a2-3
			paths.append(1)
		else:
			a2 = d0-9
			x = 0+4
			a2 = 5/a2
			paths.append(2)
		if x >= 0:
			a2 = 6-6
			d0 = a2*a2
			paths.append(3)
		else:
			a2 = 1/6
			paths.append(4)
		paths.append(5)
		assert d0 >= 0
		a2 = d0**0.5
		return a2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))