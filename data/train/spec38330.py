import numpy as np 

def function(x):

	y0 = 3
	r9 = x
	paths = []
	try:
		if y0 < 7:
			x = x-y0
			paths.append(1)
		else:
			x = x+2
			paths.append(2)
		if r9 < 2:
			r9 = r9-y0
			x = 7+2
			paths.append(3)
		else:
			x = x*x
			x = x/4
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