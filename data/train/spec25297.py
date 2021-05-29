import numpy as np 

def function(x):

	b4 = 6
	b7 = 9
	paths = []
	try:
		if x <= 3:
			b4 = 8-b4
			x = 2-b7
			paths.append(1)
		else:
			b7 = b7+6
			x = x+9
			paths.append(2)
		if b4 > 2:
			b4 = 0/x
			x = x/3
			b4 = x*b4
			paths.append(3)
		else:
			x = b7/x
			b7 = 6*b7
			b4 = b4*6
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