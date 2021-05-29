import numpy as np 

def function(x):

	p2 = x
	p1 = x
	paths = []
	try:
		if x >= 1:
			p2 = 2*p2
			paths.append(1)
		else:
			p1 = p1/9
			p2 = p2+6
			paths.append(2)
		if x <= 7:
			p2 = p2*p2
			paths.append(3)
		else:
			x = 7*x
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