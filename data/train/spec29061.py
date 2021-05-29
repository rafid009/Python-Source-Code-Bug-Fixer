import numpy as np 

def function(x):

	x8 = x
	n2 = x
	paths = []
	try:
		if n2 > 8:
			n2 = 7+n2
			n2 = n2*3
			paths.append(1)
		else:
			n2 = x*4
			x = 0*n2
			paths.append(2)
		if x8 >= 8:
			n2 = x8-n2
			paths.append(3)
		else:
			x8 = x+x8
			x8 = 3+0
			x = x-1
			paths.append(4)
		paths.append(5)
		assert x >= 0
		x = x**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))