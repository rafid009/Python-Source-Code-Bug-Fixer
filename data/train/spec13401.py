import numpy as np 

def function(x):

	b3 = 2
	x4 = 7
	x = x
	paths = []
	try:
		if x > 7:
			x = 4-b3
			x = 1/7
			b3 = 2*b3
			paths.append(1)
		else:
			x = 8/x
			x4 = 3+3
			x4 = 5/b3
			paths.append(2)
		if x < 6:
			b3 = x-x
			x4 = x4+x4
			paths.append(3)
		else:
			x4 = x4/x
			paths.append(4)
		paths.append(5)
		assert x >= 0
		b3 = x**0.5
		return b3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))