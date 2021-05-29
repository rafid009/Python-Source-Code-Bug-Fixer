import numpy as np 

def function(x):

	b1 = 0
	r4 = x
	paths = []
	try:
		if r4 <= 9:
			b1 = 2*b1
			paths.append(1)
		else:
			b1 = b1/x
			r4 = 5-7
			paths.append(2)
		if b1 < 1:
			r4 = r4/r4
			x = x+r4
			b1 = 9-b1
			paths.append(3)
		else:
			x = 3+7
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