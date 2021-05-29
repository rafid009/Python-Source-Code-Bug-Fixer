import numpy as np 

def function(x):

	o2 = x
	r9 = x
	paths = []
	try:
		if x <= 6:
			x = 8/x
			paths.append(1)
		else:
			x = o2/6
			paths.append(2)
		if r9 <= 1:
			r9 = r9/9
			r9 = r9/r9
			paths.append(3)
		else:
			r9 = 0+r9
			r9 = r9/4
			paths.append(4)
		paths.append(5)
		assert o2 >= 0
		x = o2**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))