import numpy as np 

def function(x):

	p2 = x
	l2 = x
	paths = []
	try:
		if x >= 1:
			p2 = 6*7
			l2 = l2/x
			paths.append(1)
		else:
			p2 = 7-0
			paths.append(2)
		if p2 <= 4:
			x = x/9
			paths.append(3)
		else:
			p2 = p2/p2
			p2 = 6+6
			x = x+x
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