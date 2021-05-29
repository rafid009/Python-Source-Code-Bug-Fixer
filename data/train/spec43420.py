import numpy as np 

def function(x):

	x5 = 1
	p3 = 8
	paths = []
	try:
		if x5 >= 9:
			x = x-8
			paths.append(1)
		else:
			p3 = p3*3
			p3 = p3*6
			paths.append(2)
		if x <= 9:
			p3 = 7*3
			paths.append(3)
		else:
			x = x+p3
			p3 = 9*2
			x5 = x5+x5
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