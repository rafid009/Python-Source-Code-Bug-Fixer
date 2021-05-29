import numpy as np 

def function(x):

	r9 = x
	y0 = 9
	x = x
	paths = []
	try:
		if y0 >= 4:
			r9 = r9/r9
			x = x+2
			r9 = 4*3
			paths.append(1)
		else:
			r9 = 2-r9
			paths.append(2)
		if r9 <= 5:
			y0 = y0+x
			r9 = 4+r9
			y0 = y0+y0
			paths.append(3)
		else:
			r9 = 5+1
			paths.append(4)
		paths.append(5)
		assert x >= 0
		r9 = x**0.5
		return r9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))