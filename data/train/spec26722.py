import numpy as np 

def function(x):

	n6 = x
	p9 = 1
	paths = []
	try:
		if x <= 2:
			n6 = x+n6
			p9 = 0*n6
			paths.append(1)
		else:
			n6 = p9-5
			n6 = n6*2
			paths.append(2)
		if n6 > 5:
			n6 = n6-3
			x = 1/p9
			p9 = p9+n6
			paths.append(3)
		else:
			p9 = p9*3
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