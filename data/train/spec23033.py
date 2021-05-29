import numpy as np 

def function(x):

	p2 = 8
	e9 = 3
	paths = []
	try:
		if p2 < 9:
			p2 = p2-3
			paths.append(1)
		else:
			e9 = e9*2
			e9 = 4/e9
			e9 = e9+4
			paths.append(2)
		if e9 < 8:
			p2 = 7-e9
			paths.append(3)
		else:
			x = p2-p2
			x = 4+x
			p2 = p2/x
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