import numpy as np 

def function(x):

	o9 = x
	p2 = 7
	paths = []
	try:
		if x >= 1:
			x = x-9
			p2 = 1/p2
			p2 = p2+o9
			paths.append(1)
		else:
			p2 = 4-x
			paths.append(2)
		if x >= 2:
			x = x/4
			x = x+x
			o9 = 7-9
			paths.append(3)
		else:
			x = 0/x
			x = o9/8
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