import numpy as np 

def function(x):

	r2 = x
	r4 = 3
	x = 1
	paths = []
	try:
		if x >= 7:
			r2 = 2+x
			x = x-x
			paths.append(1)
		else:
			x = x-1
			r2 = 2*r2
			paths.append(2)
		if r2 >= 1:
			x = 4*3
			r4 = r2-x
			x = 7/6
			paths.append(3)
		else:
			r4 = r4*3
			r4 = x+4
			r2 = r2/r2
			paths.append(4)
		paths.append(5)
		assert r4 >= 0
		r4 = r4**0.5
		return r4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))