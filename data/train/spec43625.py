import numpy as np 

def function(x):

	p9 = x
	y6 = x
	paths = []
	try:
		if x >= 2:
			p9 = p9-4
			paths.append(1)
		else:
			x = 1-y6
			x = x*p9
			p9 = p9+8
			paths.append(2)
		if x >= 6:
			y6 = x+x
			x = 2+4
			paths.append(3)
		else:
			x = p9/p9
			paths.append(4)
		paths.append(5)
		assert y6 >= 0
		p9 = y6**0.5
		return p9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))