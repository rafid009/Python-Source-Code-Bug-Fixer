import numpy as np 

def function(x):

	d0 = x
	a2 = 5
	paths = []
	try:
		if x > 9:
			d0 = 4/x
			x = x-a2
			paths.append(1)
		else:
			d0 = x/4
			a2 = d0*9
			paths.append(2)
		if x < 8:
			a2 = a2+8
			d0 = d0-3
			paths.append(3)
		else:
			a2 = a2/x
			x = 7*4
			a2 = 8*3
			paths.append(4)
		paths.append(5)
		assert x >= 0
		a2 = x**0.5
		return a2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))