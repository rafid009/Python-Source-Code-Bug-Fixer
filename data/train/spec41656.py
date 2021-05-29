import numpy as np 

def function(x):

	l4 = 4
	i7 = 1
	paths = []
	try:
		if i7 <= 2:
			i7 = 7/i7
			i7 = l4-i7
			paths.append(1)
		else:
			i7 = i7+9
			i7 = 6*l4
			paths.append(2)
		if x < 2:
			x = x-i7
			i7 = i7-0
			paths.append(3)
		else:
			x = 8*3
			l4 = 8/l4
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