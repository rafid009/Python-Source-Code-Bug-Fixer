import numpy as np 

def function(x):

	b7 = x
	n0 = x
	paths = []
	try:
		if b7 >= 7:
			n0 = n0+8
			x = x/x
			x = x*9
			paths.append(1)
		else:
			b7 = 7+2
			x = x+x
			b7 = 2/b7
			paths.append(2)
		if x > 4:
			n0 = x*n0
			b7 = 8/b7
			x = x*x
			paths.append(3)
		else:
			b7 = b7/3
			x = 4-3
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