import numpy as np 

def function(x):

	a2 = 6
	n8 = x
	paths = []
	try:
		if a2 <= 0:
			n8 = x+n8
			a2 = 8*x
			n8 = n8/x
			paths.append(1)
		else:
			n8 = n8*x
			paths.append(2)
		if a2 <= 2:
			a2 = a2-a2
			x = 0+4
			paths.append(3)
		else:
			n8 = 9/7
			n8 = 5-n8
			n8 = n8-0
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