import numpy as np 

def function(x):

	b1 = x
	o7 = x
	paths = []
	try:
		if x >= 6:
			x = 9*9
			b1 = b1-3
			paths.append(1)
		else:
			o7 = o7-8
			x = x+6
			paths.append(2)
		if b1 <= 7:
			o7 = o7-x
			o7 = 1*4
			paths.append(3)
		else:
			o7 = 1-8
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