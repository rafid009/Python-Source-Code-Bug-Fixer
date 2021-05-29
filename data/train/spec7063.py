import numpy as np 

def function(x):

	x1 = x
	b0 = 1
	paths = []
	try:
		if x1 >= 9:
			b0 = 2-8
			b0 = x+b0
			x = x*x
			paths.append(1)
		else:
			b0 = 7/5
			b0 = 0-0
			b0 = 3+b0
			paths.append(2)
		if x < 7:
			x = x*6
			paths.append(3)
		else:
			x = b0+x1
			b0 = b0*2
			b0 = 3-x
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