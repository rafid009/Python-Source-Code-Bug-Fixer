import numpy as np 

def function(x):

	f5 = 2
	n8 = 9
	paths = []
	try:
		if x > 3:
			f5 = 6*f5
			f5 = 2*8
			n8 = 6/n8
			paths.append(1)
		else:
			x = x-4
			paths.append(2)
		if x <= 6:
			n8 = n8+0
			n8 = n8+2
			x = x+3
			paths.append(3)
		else:
			f5 = 7/f5
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