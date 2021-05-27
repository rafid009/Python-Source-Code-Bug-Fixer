import numpy as np 

def function(x):

	y1 = 0
	b8 = 6
	paths = []
	try:
		if y1 < 2:
			b8 = 5+6
			b8 = b8*8
			paths.append(1)
		else:
			b8 = 4-8
			x = b8/4
			y1 = b8*0
			paths.append(2)
		if y1 > 0:
			y1 = y1-y1
			paths.append(3)
		else:
			x = 5-x
			y1 = 4*x
			paths.append(4)
		paths.append(5)
		assert y1 >= 0
		x = y1**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))