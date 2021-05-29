import numpy as np 

def function(x):

	y1 = 9
	r8 = 4
	paths = []
	try:
		if x < 5:
			r8 = r8-7
			paths.append(1)
		else:
			y1 = 5-r8
			r8 = r8*4
			y1 = 3+2
			paths.append(2)
		if y1 > 9:
			x = 4+5
			y1 = y1+4
			paths.append(3)
		else:
			r8 = r8*y1
			paths.append(4)
		paths.append(5)
		assert x >= 0
		r8 = x**0.5
		return r8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))