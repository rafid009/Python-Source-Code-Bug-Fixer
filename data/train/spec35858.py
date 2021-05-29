import numpy as np 

def function(x):

	g2 = x
	n1 = 5
	paths = []
	try:
		if x < 3:
			n1 = 2*2
			g2 = 6-n1
			paths.append(1)
		else:
			n1 = n1-8
			paths.append(2)
		if x >= 3:
			x = x/g2
			x = 0*x
			paths.append(3)
		else:
			n1 = 5+n1
			paths.append(4)
		paths.append(5)
		assert x >= 0
		n1 = x**0.5
		return n1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))