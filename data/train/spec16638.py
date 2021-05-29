import numpy as np 

def function(x):

	b4 = 0
	y0 = 9
	paths = []
	try:
		if b4 >= 0:
			x = x+x
			b4 = b4/y0
			x = x+6
			paths.append(1)
		else:
			x = x/b4
			b4 = b4-2
			paths.append(2)
		if y0 < 6:
			b4 = 3+x
			paths.append(3)
		else:
			x = y0+x
			y0 = 7+y0
			y0 = y0/7
			paths.append(4)
		paths.append(5)
		assert x >= 0
		b4 = x**0.5
		return b4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))