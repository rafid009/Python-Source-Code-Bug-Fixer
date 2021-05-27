import numpy as np 

def function(x):

	e0 = x
	p2 = x
	paths = []
	try:
		if p2 >= 2:
			p2 = x+p2
			paths.append(1)
		else:
			p2 = 0-p2
			paths.append(2)
		if e0 >= 1:
			x = 4-p2
			paths.append(3)
		else:
			e0 = e0-9
			paths.append(4)
		paths.append(5)
		assert p2 >= 0
		x = p2**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))