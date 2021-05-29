import numpy as np 

def function(x):

	i3 = x
	b8 = 8
	paths = []
	try:
		if b8 > 9:
			b8 = b8*9
			paths.append(1)
		else:
			b8 = 1-b8
			paths.append(2)
		if x < 3:
			x = x-8
			b8 = b8/1
			b8 = 4-b8
			paths.append(3)
		else:
			i3 = i3*b8
			x = 0-b8
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