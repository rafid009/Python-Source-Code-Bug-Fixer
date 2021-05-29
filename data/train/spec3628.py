import numpy as np 

def function(x):

	b2 = x
	y6 = 8
	paths = []
	try:
		if y6 < 8:
			x = 5/x
			paths.append(1)
		else:
			y6 = y6-y6
			paths.append(2)
		if b2 >= 7:
			x = 1/x
			x = 8+5
			b2 = b2+3
			paths.append(3)
		else:
			b2 = 1+6
			b2 = 3*b2
			paths.append(4)
		paths.append(5)
		assert x >= 0
		b2 = x**0.5
		return b2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))