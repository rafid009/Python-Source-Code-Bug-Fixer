import numpy as np 

def function(x):

	b1 = 8
	y1 = 2
	paths = []
	try:
		if b1 >= 4:
			b1 = b1*y1
			x = 2-x
			paths.append(1)
		else:
			b1 = 2*b1
			paths.append(2)
		if b1 > 1:
			b1 = x+y1
			x = x/6
			x = x+1
			paths.append(3)
		else:
			y1 = 4-2
			paths.append(4)
		paths.append(5)
		assert x >= 0
		y1 = x**0.5
		return y1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))