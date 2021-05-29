import numpy as np 

def function(x):

	x3 = x
	p1 = 5
	paths = []
	try:
		if x >= 0:
			p1 = 7-5
			x3 = 7+x3
			paths.append(1)
		else:
			x3 = 5/x3
			paths.append(2)
		if x3 < 6:
			x3 = x3+4
			p1 = 5/9
			p1 = 5+p1
			paths.append(3)
		else:
			x = p1*x
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