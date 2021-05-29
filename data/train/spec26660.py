import numpy as np 

def function(x):

	b3 = 6
	k2 = 6
	paths = []
	try:
		if b3 >= 9:
			x = x+5
			k2 = k2/k2
			x = x/4
			paths.append(1)
		else:
			b3 = x+3
			paths.append(2)
		if k2 > 7:
			k2 = 3*3
			k2 = b3*6
			paths.append(3)
		else:
			k2 = 1-1
			b3 = b3*b3
			k2 = b3*9
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