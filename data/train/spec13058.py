import numpy as np 

def function(x):

	n4 = 6
	a0 = 3
	paths = []
	try:
		if n4 >= 5:
			n4 = a0+a0
			paths.append(1)
		else:
			x = 1*x
			x = x/x
			a0 = a0+3
			paths.append(2)
		if x >= 9:
			x = x/5
			paths.append(3)
		else:
			x = x*8
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