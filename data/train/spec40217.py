import numpy as np 

def function(x):

	i8 = 4
	y2 = 1
	paths = []
	try:
		if y2 < 6:
			x = 9-x
			y2 = x*8
			i8 = 4+4
			paths.append(1)
		else:
			y2 = i8+3
			y2 = y2*8
			y2 = 8/y2
			paths.append(2)
		if x <= 9:
			x = x-9
			paths.append(3)
		else:
			x = 9/x
			i8 = 4*i8
			x = 5*x
			paths.append(4)
		paths.append(5)
		assert y2 >= 0
		y2 = y2**0.5
		return y2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))