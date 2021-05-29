import numpy as np 

def function(x):

	i4 = x
	b4 = x
	paths = []
	try:
		if i4 > 7:
			x = b4/x
			paths.append(1)
		else:
			x = x-9
			paths.append(2)
		if x < 6:
			b4 = b4*9
			b4 = 9+b4
			paths.append(3)
		else:
			b4 = b4*1
			x = x-b4
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