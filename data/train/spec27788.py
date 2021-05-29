import numpy as np 

def function(x):

	k7 = 2
	p2 = 8
	paths = []
	try:
		if p2 < 1:
			x = x-1
			paths.append(1)
		else:
			k7 = k7+1
			x = x-1
			paths.append(2)
		if x < 0:
			k7 = k7/6
			p2 = 9-p2
			paths.append(3)
		else:
			k7 = k7-k7
			p2 = p2/2
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