import numpy as np 

def function(x):

	y2 = 8
	r9 = 7
	paths = []
	try:
		if y2 >= 2:
			x = 9*x
			r9 = r9-8
			x = x-x
			paths.append(1)
		else:
			y2 = 0/y2
			paths.append(2)
		if y2 > 9:
			r9 = y2-r9
			paths.append(3)
		else:
			x = 9*x
			y2 = 4*8
			paths.append(4)
		paths.append(5)
		assert r9 >= 0
		r9 = r9**0.5
		return r9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))