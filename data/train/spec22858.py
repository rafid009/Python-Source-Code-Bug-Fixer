import numpy as np 

def function(x):

	x4 = x
	l0 = x
	paths = []
	try:
		if l0 >= 9:
			x = l0/x
			x = 1/x
			x4 = 9*4
			paths.append(1)
		else:
			x = x-2
			x = x/6
			l0 = l0+x
			paths.append(2)
		if x < 6:
			x = x4+x4
			paths.append(3)
		else:
			x4 = x4/5
			x4 = x4/7
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