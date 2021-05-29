import numpy as np 

def function(x):

	b3 = 2
	x0 = 2
	paths = []
	try:
		if x < 2:
			x0 = 6-1
			b3 = 2/9
			paths.append(1)
		else:
			x0 = x0+5
			b3 = x0+8
			b3 = 7*b3
			paths.append(2)
		if x0 > 2:
			x = x*6
			b3 = b3+x
			b3 = x0-5
			paths.append(3)
		else:
			b3 = b3+9
			paths.append(4)
		paths.append(5)
		assert x >= 0
		x0 = x**0.5
		return x0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))