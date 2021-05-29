import numpy as np 

def function(x):

	y4 = x
	w5 = 9
	paths = []
	try:
		if w5 > 1:
			w5 = w5*w5
			paths.append(1)
		else:
			x = x/y4
			y4 = 6+9
			paths.append(2)
		if w5 > 1:
			y4 = 6+1
			paths.append(3)
		else:
			y4 = y4/y4
			x = x/6
			x = y4*8
			paths.append(4)
		paths.append(5)
		assert x >= 0
		x = x**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))