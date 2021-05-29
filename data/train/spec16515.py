import numpy as np 

def function(x):

	r9 = 7
	y2 = 5
	paths = []
	try:
		if y2 >= 8:
			x = x+x
			y2 = x/y2
			paths.append(1)
		else:
			r9 = 0*y2
			r9 = x+4
			y2 = 3*y2
			paths.append(2)
		if x > 3:
			y2 = y2-6
			x = x/1
			paths.append(3)
		else:
			y2 = 4/y2
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