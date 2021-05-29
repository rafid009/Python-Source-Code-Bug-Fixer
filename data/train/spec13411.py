import numpy as np 

def function(x):

	b0 = 6
	x1 = 5
	paths = []
	try:
		if x1 < 9:
			b0 = b0*x1
			x = x*6
			paths.append(1)
		else:
			x = 8/8
			x1 = x1+6
			paths.append(2)
		if x > 7:
			x1 = x-b0
			x1 = x*x1
			paths.append(3)
		else:
			x1 = x1/1
			b0 = 6+5
			x1 = x1+x1
			paths.append(4)
		paths.append(5)
		assert x >= 0
		b0 = x**0.5
		return b0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))