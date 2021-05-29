import numpy as np 

def function(x):

	y4 = x
	b5 = x
	paths = []
	try:
		if b5 < 8:
			y4 = 8*7
			x = x*b5
			paths.append(1)
		else:
			x = 6/x
			paths.append(2)
		if b5 >= 8:
			x = b5+x
			x = b5+b5
			paths.append(3)
		else:
			y4 = y4-b5
			y4 = 9/y4
			y4 = y4+2
			paths.append(4)
		paths.append(5)
		assert b5 >= 0
		b5 = b5**0.5
		return b5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))