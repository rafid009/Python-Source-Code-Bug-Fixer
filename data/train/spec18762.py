import numpy as np 

def function(x):

	n0 = x
	r2 = 4
	paths = []
	try:
		if n0 >= 0:
			r2 = r2+6
			n0 = n0/7
			r2 = 7-4
			paths.append(1)
		else:
			n0 = n0+8
			paths.append(2)
		if r2 <= 4:
			r2 = r2/1
			paths.append(3)
		else:
			r2 = r2/3
			paths.append(4)
		paths.append(5)
		assert n0 >= 0
		r2 = n0**0.5
		return r2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))