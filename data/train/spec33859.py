import numpy as np 

def function(x):

	r2 = 6
	n8 = 1
	paths = []
	try:
		if r2 > 1:
			n8 = 6+n8
			n8 = n8+0
			n8 = 8/n8
			paths.append(1)
		else:
			x = 1-x
			paths.append(2)
		if x < 9:
			n8 = 7-1
			n8 = x*n8
			x = 3+x
			paths.append(3)
		else:
			r2 = x/r2
			r2 = 7+3
			paths.append(4)
		paths.append(5)
		assert x >= 0
		n8 = x**0.5
		return n8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))