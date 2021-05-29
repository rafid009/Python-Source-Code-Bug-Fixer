import numpy as np 

def function(x):

	r7 = 6
	r9 = 7
	paths = []
	try:
		if x >= 8:
			r9 = 0-r9
			r7 = x+8
			x = 1+r9
			paths.append(1)
		else:
			r7 = 2-r9
			r7 = r9+0
			paths.append(2)
		if r7 > 9:
			r9 = 1*r9
			x = r9/r7
			x = 7-1
			paths.append(3)
		else:
			x = x*8
			paths.append(4)
		paths.append(5)
		assert x >= 0
		r7 = x**0.5
		return r7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))