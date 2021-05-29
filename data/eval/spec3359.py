import numpy as np 

def function(x):

	j8 = 9
	n5 = 9
	paths = []
	try:
		if n5 >= 9:
			n5 = x*4
			paths.append(1)
		else:
			n5 = n5/3
			j8 = j8-j8
			n5 = 6+n5
			paths.append(2)
		if x > 9:
			x = 9+6
			x = 3/x
			x = n5*x
			paths.append(3)
		else:
			j8 = j8/2
			x = x-3
			paths.append(4)
		paths.append(5)
		assert x >= 0
		n5 = x**0.5
		return n5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))