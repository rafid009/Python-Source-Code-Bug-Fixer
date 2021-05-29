import numpy as np 

def function(x):

	y5 = x
	b8 = x
	paths = []
	try:
		if y5 >= 7:
			x = y5-x
			b8 = 6-b8
			paths.append(1)
		else:
			x = x*b8
			x = x*4
			paths.append(2)
		if x >= 1:
			x = y5-y5
			paths.append(3)
		else:
			y5 = 2+9
			paths.append(4)
		paths.append(5)
		assert y5 >= 0
		x = y5**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))