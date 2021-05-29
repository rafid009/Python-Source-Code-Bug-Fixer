import numpy as np 

def function(x):

	p2 = 9
	e0 = 1
	paths = []
	try:
		if x <= 6:
			e0 = e0-x
			paths.append(1)
		else:
			e0 = p2-3
			paths.append(2)
		if x <= 4:
			p2 = 6-p2
			p2 = p2*5
			paths.append(3)
		else:
			p2 = p2+7
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