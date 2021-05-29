import numpy as np 

def function(x):

	e2 = x
	p7 = 4
	paths = []
	try:
		if x <= 1:
			p7 = e2+p7
			p7 = 5-p7
			p7 = 8/9
			paths.append(1)
		else:
			p7 = p7+8
			paths.append(2)
		if x <= 7:
			x = 6/x
			paths.append(3)
		else:
			p7 = e2+p7
			x = e2/x
			x = 3/x
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