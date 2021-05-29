import numpy as np 

def function(x):

	l0 = 4
	x1 = x
	paths = []
	try:
		if l0 > 2:
			x1 = 9/x1
			paths.append(1)
		else:
			l0 = 7*4
			paths.append(2)
		if x1 <= 5:
			x1 = x1+x
			x1 = x1-l0
			x1 = x1-5
			paths.append(3)
		else:
			x = 1/x
			paths.append(4)
		paths.append(5)
		assert x1 >= 0
		x = x1**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))