import numpy as np 

def function(x):

	x2 = x
	b2 = 2
	paths = []
	try:
		if b2 >= 9:
			x2 = x/9
			x2 = 4-x2
			x = x-b2
			paths.append(1)
		else:
			x2 = 1*x2
			x = 9*x
			x = 8*x
			paths.append(2)
		if b2 < 3:
			x2 = x2/7
			x2 = 8/x2
			paths.append(3)
		else:
			b2 = 8/1
			x = 5*x
			paths.append(4)
		paths.append(5)
		assert x >= 0
		b2 = x**0.5
		return b2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))