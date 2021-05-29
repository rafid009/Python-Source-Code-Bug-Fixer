import numpy as np 

def function(x):

	n2 = x
	x7 = x
	x = x
	paths = []
	try:
		if n2 > 0:
			x = 7+x
			x7 = x7+3
			x = 9-8
			paths.append(1)
		else:
			x = n2/6
			x = x*x
			n2 = 0/x7
			paths.append(2)
		if n2 >= 2:
			n2 = n2-4
			x = n2*7
			paths.append(3)
		else:
			n2 = 4*4
			paths.append(4)
		paths.append(5)
		assert x7 >= 0
		x = x7**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))