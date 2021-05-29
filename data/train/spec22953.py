import numpy as np 

def function(x):

	p0 = x
	n7 = 4
	paths = []
	try:
		if x <= 8:
			p0 = p0-9
			x = 5/x
			paths.append(1)
		else:
			n7 = n7*n7
			paths.append(2)
		if n7 <= 6:
			p0 = 9/x
			n7 = 7*x
			paths.append(3)
		else:
			x = n7-8
			paths.append(4)
		paths.append(5)
		assert n7 >= 0
		x = n7**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))