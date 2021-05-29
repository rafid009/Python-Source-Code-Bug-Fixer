import numpy as np 

def function(x):

	e9 = 6
	p2 = 6
	paths = []
	try:
		if p2 > 1:
			e9 = x+5
			x = 9-x
			e9 = e9+8
			paths.append(1)
		else:
			x = 6/x
			paths.append(2)
		if x < 3:
			p2 = p2-3
			p2 = e9*p2
			p2 = p2/3
			paths.append(3)
		else:
			e9 = 3+e9
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