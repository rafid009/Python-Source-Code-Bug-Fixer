import numpy as np 

def function(x):

	i9 = x
	b8 = x
	paths = []
	try:
		if b8 >= 6:
			x = x/i9
			paths.append(1)
		else:
			i9 = 5/9
			x = x-6
			paths.append(2)
		if x < 5:
			i9 = i9*b8
			i9 = i9-2
			x = b8-1
			paths.append(3)
		else:
			x = 1+x
			x = 3+7
			paths.append(4)
		paths.append(5)
		assert x >= 0
		b8 = x**0.5
		return b8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))