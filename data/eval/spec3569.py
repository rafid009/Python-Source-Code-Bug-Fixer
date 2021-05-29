import numpy as np 

def function(x):

	b1 = 6
	x9 = x
	paths = []
	try:
		if b1 >= 1:
			x9 = x9+2
			paths.append(1)
		else:
			x9 = x9-4
			b1 = b1-x
			paths.append(2)
		if x9 <= 9:
			b1 = b1-1
			x = b1/x
			b1 = b1+9
			paths.append(3)
		else:
			x9 = x9/b1
			x = 8+b1
			x9 = x9*4
			paths.append(4)
		paths.append(5)
		assert x9 >= 0
		x9 = x9**0.5
		return x9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))