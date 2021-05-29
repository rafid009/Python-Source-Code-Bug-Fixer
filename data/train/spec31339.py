import numpy as np 

def function(x):

	p6 = 1
	x7 = x
	paths = []
	try:
		if x < 3:
			x7 = 7*4
			x7 = 9/x7
			x7 = 0-2
			paths.append(1)
		else:
			x = 4/x7
			x = x7*7
			paths.append(2)
		if p6 > 2:
			p6 = 9+2
			x7 = x7/p6
			p6 = p6-9
			paths.append(3)
		else:
			x = p6/x
			x7 = x7*9
			paths.append(4)
		paths.append(5)
		assert x7 >= 0
		x7 = x7**0.5
		return x7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))