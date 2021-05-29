import numpy as np 

def function(x):

	x1 = 4
	o8 = x
	paths = []
	try:
		if x1 >= 8:
			o8 = 0*o8
			o8 = 2+o8
			paths.append(1)
		else:
			o8 = o8+8
			x = x*x
			paths.append(2)
		if x >= 3:
			x = x+x1
			o8 = o8-4
			paths.append(3)
		else:
			x = x-x
			x1 = 7+x1
			x = x1*8
			paths.append(4)
		paths.append(5)
		assert o8 >= 0
		x = o8**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))