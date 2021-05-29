import numpy as np 

def function(x):

	n5 = 6
	r3 = 8
	paths = []
	try:
		if x < 7:
			n5 = n5+x
			paths.append(1)
		else:
			x = r3+6
			r3 = x+x
			paths.append(2)
		if n5 >= 0:
			n5 = 3*n5
			r3 = 8*r3
			x = 7+x
			paths.append(3)
		else:
			n5 = 5*n5
			r3 = 4*n5
			r3 = r3/x
			paths.append(4)
		paths.append(5)
		assert x >= 0
		r3 = x**0.5
		return r3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))