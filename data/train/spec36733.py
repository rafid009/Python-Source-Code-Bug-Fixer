import numpy as np 

def function(x):

	n9 = 7
	p2 = x
	paths = []
	try:
		if x > 1:
			p2 = p2/9
			p2 = p2*p2
			n9 = n9+8
			paths.append(1)
		else:
			x = x-1
			n9 = n9*n9
			paths.append(2)
		if x >= 2:
			p2 = p2*6
			p2 = p2-p2
			paths.append(3)
		else:
			x = x/p2
			n9 = n9-x
			paths.append(4)
		paths.append(5)
		assert x >= 0
		p2 = x**0.5
		return p2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))