import numpy as np 

def function(x):

	b5 = x
	k4 = x
	paths = []
	try:
		if b5 <= 9:
			b5 = 2+x
			x = k4*4
			paths.append(1)
		else:
			k4 = 3/k4
			b5 = 1/b5
			k4 = b5-0
			paths.append(2)
		if b5 >= 6:
			k4 = 7+k4
			paths.append(3)
		else:
			b5 = 0+8
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