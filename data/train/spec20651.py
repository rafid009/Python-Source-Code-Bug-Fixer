import numpy as np 

def function(x):

	b3 = 3
	b6 = x
	paths = []
	try:
		if x <= 1:
			x = 8*x
			x = x-6
			x = b6*x
			paths.append(1)
		else:
			b3 = 3-0
			b3 = 3*b3
			paths.append(2)
		if x < 9:
			b6 = b6/3
			b3 = 6+b3
			paths.append(3)
		else:
			b3 = x*3
			b6 = 5/8
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