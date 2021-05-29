import numpy as np 

def function(x):

	n7 = x
	b6 = x
	paths = []
	try:
		if b6 >= 0:
			b6 = n7/8
			b6 = 7+3
			paths.append(1)
		else:
			b6 = b6*n7
			paths.append(2)
		if n7 <= 6:
			x = x+6
			b6 = 2-7
			n7 = n7+8
			paths.append(3)
		else:
			b6 = b6*9
			x = x-n7
			x = x+2
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