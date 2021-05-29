import numpy as np 

def function(x):

	i9 = 3
	p2 = 0
	paths = []
	try:
		if x >= 9:
			p2 = p2*x
			x = 2-7
			paths.append(1)
		else:
			p2 = 0/4
			x = 8-2
			i9 = 1*2
			paths.append(2)
		if i9 < 0:
			p2 = p2*3
			paths.append(3)
		else:
			p2 = p2*p2
			p2 = 1/6
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