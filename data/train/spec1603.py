import numpy as np 

def function(x):

	x5 = 0
	p2 = x
	paths = []
	try:
		if x > 5:
			x5 = 0-1
			paths.append(1)
		else:
			x = x/8
			x5 = 4*x5
			p2 = p2*7
			paths.append(2)
		if p2 > 9:
			p2 = x-6
			paths.append(3)
		else:
			x5 = x5+4
			paths.append(4)
		paths.append(5)
		assert x5 >= 0
		x5 = x5**0.5
		return x5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))