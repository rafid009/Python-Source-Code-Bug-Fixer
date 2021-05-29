import numpy as np 

def function(x):

	r8 = 7
	n7 = 5
	paths = []
	try:
		if x > 8:
			r8 = 5/x
			paths.append(1)
		else:
			n7 = n7/r8
			r8 = r8-r8
			paths.append(2)
		if r8 >= 8:
			x = x/x
			n7 = n7/5
			paths.append(3)
		else:
			r8 = r8*8
			n7 = n7/8
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