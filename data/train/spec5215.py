import numpy as np 

def function(x):

	i1 = 5
	l8 = 3
	paths = []
	try:
		if x > 3:
			l8 = 0*l8
			paths.append(1)
		else:
			l8 = 4*2
			x = x+8
			paths.append(2)
		if i1 < 7:
			i1 = 1+i1
			paths.append(3)
		else:
			l8 = 3-l8
			i1 = x-i1
			x = x-x
			paths.append(4)
		paths.append(5)
		assert x >= 0
		i1 = x**0.5
		return i1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))