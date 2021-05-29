import numpy as np 

def function(x):

	r4 = 9
	x9 = 3
	x = x
	paths = []
	try:
		if x < 7:
			x9 = x9+0
			x = 7+4
			r4 = 0/x9
			paths.append(1)
		else:
			r4 = 0+r4
			x9 = x9-x9
			x9 = 1-7
			paths.append(2)
		if x < 0:
			x9 = x9-0
			x = 8-r4
			paths.append(3)
		else:
			r4 = 3-r4
			x = x*x
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