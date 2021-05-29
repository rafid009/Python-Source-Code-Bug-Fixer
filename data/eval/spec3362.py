import numpy as np 

def function(x):

	b5 = 4
	i0 = 1
	paths = []
	try:
		if b5 > 9:
			x = 1+4
			paths.append(1)
		else:
			i0 = 8/i0
			i0 = 9/i0
			paths.append(2)
		if b5 < 9:
			i0 = i0/b5
			b5 = 9*3
			x = b5/x
			paths.append(3)
		else:
			i0 = i0*7
			b5 = 7+b5
			i0 = i0*9
			paths.append(4)
		paths.append(5)
		assert x >= 0
		i0 = x**0.5
		return i0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))