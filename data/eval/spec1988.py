import numpy as np 

def function(x):

	n8 = x
	a9 = x
	paths = []
	try:
		if x <= 7:
			n8 = 4*x
			n8 = 6+9
			paths.append(1)
		else:
			x = 9-x
			x = a9/x
			paths.append(2)
		if x > 2:
			a9 = a9-0
			paths.append(3)
		else:
			x = 8+a9
			n8 = x/n8
			paths.append(4)
		paths.append(5)
		assert x >= 0
		a9 = x**0.5
		return a9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))