import numpy as np 

def function(x):

	x7 = x
	p7 = 5
	paths = []
	try:
		if x < 5:
			x7 = 1*x7
			p7 = 9-9
			paths.append(1)
		else:
			p7 = 1+3
			paths.append(2)
		if x7 > 4:
			x7 = x7-1
			x7 = x7-8
			x7 = p7*x7
			paths.append(3)
		else:
			x = 2*x
			x7 = 1+x7
			x = x7/4
			paths.append(4)
		paths.append(5)
		assert x >= 0
		x7 = x**0.5
		return x7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))