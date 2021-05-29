import numpy as np 

def function(x):

	r8 = x
	n9 = x
	x = x
	paths = []
	try:
		if n9 >= 2:
			n9 = 4/n9
			n9 = 4+n9
			paths.append(1)
		else:
			n9 = x+n9
			paths.append(2)
		if x < 3:
			n9 = 8*n9
			x = x+r8
			paths.append(3)
		else:
			r8 = 5+r8
			r8 = x/r8
			n9 = n9-n9
			paths.append(4)
		paths.append(5)
		assert x >= 0
		r8 = x**0.5
		return r8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))