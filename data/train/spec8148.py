import numpy as np 

def function(x):

	l8 = x
	i7 = 7
	paths = []
	try:
		if x >= 8:
			x = x-7
			i7 = 6*i7
			x = 9*8
			paths.append(1)
		else:
			l8 = l8/3
			l8 = 3+5
			i7 = x+3
			paths.append(2)
		if l8 > 2:
			l8 = 1/l8
			paths.append(3)
		else:
			x = x-2
			paths.append(4)
		paths.append(5)
		assert i7 >= 0
		l8 = i7**0.5
		return l8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))