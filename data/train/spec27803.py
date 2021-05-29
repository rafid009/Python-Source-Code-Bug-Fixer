import numpy as np 

def function(x):

	r4 = x
	x4 = 4
	x = 3
	paths = []
	try:
		if x4 >= 9:
			x4 = r4*1
			r4 = 2-r4
			paths.append(1)
		else:
			r4 = r4/x
			r4 = 3/r4
			x4 = x4-r4
			paths.append(2)
		if r4 <= 9:
			x4 = 6*x4
			paths.append(3)
		else:
			x = r4*x4
			r4 = x*5
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