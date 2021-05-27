import numpy as np 

def function(x):

	p7 = x
	n1 = 4
	paths = []
	try:
		if n1 > 2:
			x = 0-3
			paths.append(1)
		else:
			n1 = 6+n1
			x = x-5
			paths.append(2)
		if n1 < 2:
			n1 = 1*4
			n1 = n1*2
			paths.append(3)
		else:
			n1 = n1/7
			n1 = x+p7
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