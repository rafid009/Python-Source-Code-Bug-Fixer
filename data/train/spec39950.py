import numpy as np 

def function(x):

	p2 = x
	n1 = x
	paths = []
	try:
		if n1 >= 2:
			x = 8*x
			p2 = x+n1
			n1 = 8/n1
			paths.append(1)
		else:
			x = 2-x
			paths.append(2)
		if n1 > 8:
			n1 = 8-x
			paths.append(3)
		else:
			x = 8+p2
			p2 = p2*4
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