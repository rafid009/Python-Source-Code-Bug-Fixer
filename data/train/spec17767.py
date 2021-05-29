import numpy as np 

def function(x):

	p9 = 2
	a8 = x
	paths = []
	try:
		if a8 <= 0:
			x = 1-3
			x = p9+x
			p9 = p9*1
			paths.append(1)
		else:
			a8 = 5-9
			p9 = 7-p9
			a8 = p9+6
			paths.append(2)
		if p9 <= 3:
			a8 = x*a8
			x = 4*x
			x = 5-a8
			paths.append(3)
		else:
			x = p9-x
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