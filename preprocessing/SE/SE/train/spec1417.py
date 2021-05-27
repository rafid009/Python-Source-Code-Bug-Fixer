import numpy as np 

def function(x):

	p4 = 2
	y3 = x
	paths = []
	try:
		if x >= 5:
			y3 = y3+x
			paths.append(1)
		else:
			y3 = y3/x
			paths.append(2)
		if p4 > 3:
			x = 7*x
			paths.append(3)
		else:
			y3 = y3/4
			x = p4-y3
			x = x/p4
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