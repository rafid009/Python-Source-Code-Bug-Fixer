import numpy as np 

def function(x):

	y5 = x
	b1 = x
	paths = []
	try:
		if b1 > 7:
			b1 = 0+5
			y5 = 9*y5
			paths.append(1)
		else:
			b1 = b1+y5
			b1 = 5/y5
			paths.append(2)
		if b1 < 3:
			b1 = 9*b1
			x = 6*b1
			b1 = b1/b1
			paths.append(3)
		else:
			y5 = 5+y5
			x = x/1
			y5 = 8-x
			paths.append(4)
		paths.append(5)
		assert y5 >= 0
		y5 = y5**0.5
		return y5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))