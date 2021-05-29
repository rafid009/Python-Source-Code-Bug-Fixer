import numpy as np 

def function(x):

	b6 = 6
	i0 = x
	paths = []
	try:
		if i0 >= 3:
			b6 = b6/6
			b6 = b6*4
			paths.append(1)
		else:
			i0 = 0-i0
			b6 = b6+b6
			paths.append(2)
		if i0 > 9:
			b6 = i0/2
			b6 = b6*x
			paths.append(3)
		else:
			b6 = 8-b6
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