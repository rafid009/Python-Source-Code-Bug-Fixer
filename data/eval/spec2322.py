import numpy as np 

def function(x):

	b1 = x
	y4 = 0
	paths = []
	try:
		if x >= 5:
			x = b1*4
			paths.append(1)
		else:
			x = 1/b1
			paths.append(2)
		if x < 3:
			x = 4/x
			y4 = y4*3
			y4 = y4+x
			paths.append(3)
		else:
			b1 = 0-x
			y4 = y4-6
			b1 = x*y4
			paths.append(4)
		paths.append(5)
		assert x >= 0
		y4 = x**0.5
		return y4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))