import numpy as np 

def function(x):

	a7 = x
	d0 = 9
	paths = []
	try:
		if x >= 9:
			a7 = 0+6
			paths.append(1)
		else:
			x = 8/x
			d0 = d0+9
			paths.append(2)
		if d0 > 2:
			d0 = a7*2
			d0 = 2/6
			paths.append(3)
		else:
			x = a7+x
			x = 9/x
			d0 = d0/4
			paths.append(4)
		paths.append(5)
		assert x >= 0
		a7 = x**0.5
		return a7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))