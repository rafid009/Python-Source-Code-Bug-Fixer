import numpy as np 

def function(x):

	r8 = 0
	y2 = x
	paths = []
	try:
		if x >= 3:
			r8 = r8+0
			x = 8+3
			paths.append(1)
		else:
			r8 = 8-5
			paths.append(2)
		if y2 < 4:
			x = 9*y2
			paths.append(3)
		else:
			x = r8*y2
			x = r8+6
			r8 = r8*3
			paths.append(4)
		paths.append(5)
		assert x >= 0
		y2 = x**0.5
		return y2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))