import numpy as np 

def function(x):

	n9 = 2
	p2 = 5
	paths = []
	try:
		if n9 <= 0:
			n9 = p2/8
			paths.append(1)
		else:
			p2 = p2*x
			n9 = 7*n9
			paths.append(2)
		if x > 0:
			x = x/9
			paths.append(3)
		else:
			p2 = p2*8
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