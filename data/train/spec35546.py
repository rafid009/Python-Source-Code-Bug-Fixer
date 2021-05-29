import numpy as np 

def function(x):

	o3 = x
	r7 = x
	x = x
	paths = []
	try:
		if x <= 5:
			o3 = o3*5
			r7 = 2/6
			r7 = r7/r7
			paths.append(1)
		else:
			r7 = x+r7
			paths.append(2)
		if x < 6:
			x = r7-4
			x = 6/x
			paths.append(3)
		else:
			r7 = o3*6
			x = 9/x
			paths.append(4)
		paths.append(5)
		assert x >= 0
		r7 = x**0.5
		return r7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))