import numpy as np 

def function(x):

	w7 = 0
	y7 = 9
	paths = []
	try:
		if y7 >= 8:
			y7 = w7+y7
			y7 = 4*y7
			y7 = 7+y7
			paths.append(1)
		else:
			y7 = 4/y7
			y7 = w7+8
			x = x*x
			paths.append(2)
		if w7 > 9:
			y7 = 1+x
			paths.append(3)
		else:
			y7 = w7*4
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