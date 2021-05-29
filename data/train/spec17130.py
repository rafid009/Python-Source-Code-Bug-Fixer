import numpy as np 

def function(x):

	a8 = x
	r4 = 7
	paths = []
	try:
		if r4 < 5:
			a8 = a8/x
			x = x/r4
			paths.append(1)
		else:
			r4 = r4+a8
			r4 = 4/r4
			paths.append(2)
		if a8 < 8:
			r4 = 9-r4
			r4 = r4/9
			x = x-6
			paths.append(3)
		else:
			a8 = a8+r4
			x = 0/x
			r4 = r4*3
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