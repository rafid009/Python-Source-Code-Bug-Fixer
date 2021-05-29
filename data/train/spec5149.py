import numpy as np 

def function(x):

	n4 = 3
	r9 = x
	paths = []
	try:
		if r9 < 4:
			r9 = r9+5
			n4 = 9+n4
			r9 = n4*r9
			paths.append(1)
		else:
			r9 = r9-7
			x = 3/x
			n4 = r9+n4
			paths.append(2)
		if n4 <= 7:
			x = x+9
			paths.append(3)
		else:
			n4 = 4-n4
			paths.append(4)
		paths.append(5)
		assert n4 >= 0
		r9 = n4**0.5
		return r9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))