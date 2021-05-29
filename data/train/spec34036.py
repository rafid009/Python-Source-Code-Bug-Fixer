import numpy as np 

def function(x):

	n8 = 2
	p8 = x
	paths = []
	try:
		if x < 2:
			x = x+3
			paths.append(1)
		else:
			n8 = 7*n8
			n8 = n8+3
			paths.append(2)
		if n8 < 1:
			x = p8-9
			p8 = p8*x
			paths.append(3)
		else:
			n8 = n8-7
			n8 = p8/7
			paths.append(4)
		paths.append(5)
		assert x >= 0
		n8 = x**0.5
		return n8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))