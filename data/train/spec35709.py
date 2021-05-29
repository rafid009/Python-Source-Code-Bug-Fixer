import numpy as np 

def function(x):

	x5 = x
	r4 = 4
	paths = []
	try:
		if x > 4:
			r4 = x5/r4
			x5 = x5+4
			x5 = 4-x5
			paths.append(1)
		else:
			x5 = 2-5
			x5 = 7/5
			x5 = x5/5
			paths.append(2)
		if x <= 6:
			x = 6/x
			r4 = r4-9
			paths.append(3)
		else:
			r4 = x5*8
			r4 = r4/x5
			x = x5-x
			paths.append(4)
		paths.append(5)
		assert r4 >= 0
		x5 = r4**0.5
		return x5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))