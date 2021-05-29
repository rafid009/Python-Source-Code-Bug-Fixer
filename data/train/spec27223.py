import numpy as np 

def function(x):

	p8 = 3
	p9 = 2
	paths = []
	try:
		if x > 6:
			p8 = p9+x
			paths.append(1)
		else:
			p9 = p9/x
			p9 = p9/p9
			paths.append(2)
		if p8 < 9:
			p9 = p9+x
			p8 = x*p8
			paths.append(3)
		else:
			x = p9+p8
			p9 = x/p9
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