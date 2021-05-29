import numpy as np 

def function(x):

	n7 = 9
	r5 = 4
	paths = []
	try:
		if x >= 0:
			r5 = 6/x
			paths.append(1)
		else:
			r5 = r5-n7
			paths.append(2)
		if n7 > 9:
			n7 = 0-9
			r5 = x*r5
			r5 = r5/7
			paths.append(3)
		else:
			n7 = x-r5
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