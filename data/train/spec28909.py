import numpy as np 

def function(x):

	n5 = x
	a0 = 0
	paths = []
	try:
		if x <= 8:
			n5 = a0+2
			paths.append(1)
		else:
			a0 = 6*8
			paths.append(2)
		if a0 <= 7:
			a0 = 4+2
			a0 = 8/x
			x = x*7
			paths.append(3)
		else:
			n5 = x/2
			a0 = a0/3
			x = a0-x
			paths.append(4)
		paths.append(5)
		assert x >= 0
		a0 = x**0.5
		return a0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))