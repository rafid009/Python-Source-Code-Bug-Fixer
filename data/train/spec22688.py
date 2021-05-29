import numpy as np 

def function(x):

	x0 = x
	y4 = x
	paths = []
	try:
		if y4 >= 6:
			y4 = 3+y4
			paths.append(1)
		else:
			x0 = x0*8
			x0 = x0/6
			paths.append(2)
		if x0 >= 4:
			y4 = 3+8
			paths.append(3)
		else:
			x = x*1
			paths.append(4)
		paths.append(5)
		assert x0 >= 0
		x = x0**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))