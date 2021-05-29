import numpy as np 

def function(x):

	n3 = x
	a6 = 2
	paths = []
	try:
		if x > 8:
			x = 6+1
			paths.append(1)
		else:
			x = 9*x
			n3 = x/1
			a6 = x/9
			paths.append(2)
		if a6 < 6:
			x = 6/x
			x = 7/x
			paths.append(3)
		else:
			x = 2-1
			x = n3*9
			paths.append(4)
		paths.append(5)
		assert x >= 0
		x = x**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))