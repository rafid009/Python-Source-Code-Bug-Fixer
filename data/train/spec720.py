import numpy as np 

def function(x):

	a9 = 5
	n0 = 1
	paths = []
	try:
		if n0 <= 4:
			n0 = n0-3
			a9 = 4-a9
			paths.append(1)
		else:
			n0 = 5-n0
			n0 = n0-a9
			n0 = n0/9
			paths.append(2)
		if a9 >= 1:
			n0 = n0/5
			n0 = n0*8
			n0 = x/x
			paths.append(3)
		else:
			a9 = a9/3
			x = 8*3
			n0 = n0-8
			paths.append(4)
		paths.append(5)
		assert n0 >= 0
		x = n0**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))