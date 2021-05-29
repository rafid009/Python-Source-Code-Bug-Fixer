import numpy as np 

def function(x):

	p3 = x
	n1 = x
	paths = []
	try:
		if n1 <= 5:
			p3 = 3/p3
			paths.append(1)
		else:
			p3 = p3*n1
			x = x/6
			paths.append(2)
		if p3 > 2:
			x = 4/3
			paths.append(3)
		else:
			x = x-3
			x = x+p3
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