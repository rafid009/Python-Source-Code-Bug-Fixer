import numpy as np 

def function(x):

	y1 = x
	b4 = x
	paths = []
	try:
		if b4 > 6:
			x = y1/y1
			paths.append(1)
		else:
			x = x+7
			paths.append(2)
		if b4 <= 8:
			x = 5+b4
			x = x-7
			b4 = b4-0
			paths.append(3)
		else:
			b4 = 0-b4
			y1 = y1+x
			paths.append(4)
		paths.append(5)
		assert y1 >= 0
		y1 = y1**0.5
		return y1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))