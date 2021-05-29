import numpy as np 

def function(x):

	r4 = x
	u2 = x
	paths = []
	try:
		if u2 < 5:
			u2 = u2*8
			paths.append(1)
		else:
			r4 = u2/3
			x = 3/u2
			u2 = 7-0
			paths.append(2)
		if u2 >= 1:
			u2 = u2+2
			paths.append(3)
		else:
			r4 = 0-r4
			paths.append(4)
		paths.append(5)
		assert x >= 0
		r4 = x**0.5
		return r4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))