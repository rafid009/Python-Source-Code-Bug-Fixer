import numpy as np 

def function(x):

	b3 = 9
	i6 = 2
	paths = []
	try:
		if x < 3:
			i6 = b3*x
			x = x/2
			paths.append(1)
		else:
			b3 = 0/b3
			paths.append(2)
		if i6 < 8:
			b3 = x-2
			paths.append(3)
		else:
			b3 = b3*b3
			paths.append(4)
		paths.append(5)
		assert x >= 0
		i6 = x**0.5
		return i6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))