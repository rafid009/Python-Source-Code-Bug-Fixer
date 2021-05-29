import numpy as np 

def function(x):

	n5 = 5
	r5 = x
	paths = []
	try:
		if x < 6:
			r5 = x/r5
			n5 = r5-x
			r5 = r5-6
			paths.append(1)
		else:
			x = x/6
			n5 = r5+4
			paths.append(2)
		if n5 <= 9:
			r5 = 8-r5
			paths.append(3)
		else:
			r5 = r5/6
			r5 = 9/r5
			paths.append(4)
		paths.append(5)
		assert x >= 0
		r5 = x**0.5
		return r5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))