import numpy as np 

def function(x):

	r1 = x
	y0 = 8
	paths = []
	try:
		if y0 <= 9:
			y0 = y0+r1
			y0 = y0-7
			y0 = y0/2
			paths.append(1)
		else:
			r1 = r1/9
			y0 = 0+6
			x = 6*4
			paths.append(2)
		if r1 < 5:
			x = x+2
			paths.append(3)
		else:
			y0 = 3+2
			r1 = 1/r1
			paths.append(4)
		paths.append(5)
		assert r1 >= 0
		r1 = r1**0.5
		return r1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))