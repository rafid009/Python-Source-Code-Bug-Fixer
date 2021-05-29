import numpy as np 

def function(x):

	b0 = 8
	i4 = x
	paths = []
	try:
		if x >= 7:
			i4 = 3/5
			b0 = b0*b0
			i4 = i4-i4
			paths.append(1)
		else:
			b0 = 8-4
			paths.append(2)
		if i4 >= 1:
			x = b0-b0
			b0 = b0*5
			x = 5*7
			paths.append(3)
		else:
			x = x*8
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