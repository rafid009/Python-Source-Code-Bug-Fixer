import numpy as np 

def function(x):

	p2 = 2
	n5 = x
	paths = []
	try:
		if p2 <= 1:
			n5 = n5/n5
			p2 = 4/p2
			paths.append(1)
		else:
			n5 = 9-6
			p2 = 2-p2
			x = 4-x
			paths.append(2)
		if p2 <= 8:
			p2 = p2+5
			paths.append(3)
		else:
			n5 = n5*n5
			x = x-3
			p2 = n5/p2
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