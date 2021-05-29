import numpy as np 

def function(x):

	p9 = 6
	x3 = 0
	paths = []
	try:
		if x <= 8:
			p9 = 8*p9
			paths.append(1)
		else:
			p9 = p9*x3
			p9 = p9/1
			x3 = 8/x
			paths.append(2)
		if x < 5:
			x = x+x
			x3 = 3*x3
			paths.append(3)
		else:
			x = 6-3
			x3 = x3+x3
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