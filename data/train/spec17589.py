import numpy as np 

def function(x):

	p2 = x
	k2 = x
	paths = []
	try:
		if x >= 9:
			x = k2-3
			k2 = x+p2
			x = 1-x
			paths.append(1)
		else:
			p2 = p2-1
			paths.append(2)
		if p2 <= 4:
			x = p2/5
			paths.append(3)
		else:
			k2 = k2-k2
			p2 = p2*p2
			k2 = x/4
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