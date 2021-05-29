import numpy as np 

def function(x):

	o5 = x
	r2 = x
	x = x
	paths = []
	try:
		if r2 < 6:
			o5 = 2-8
			paths.append(1)
		else:
			x = o5/x
			r2 = 8-o5
			paths.append(2)
		if r2 >= 2:
			r2 = r2/o5
			o5 = r2/o5
			paths.append(3)
		else:
			o5 = 0-o5
			o5 = 3-x
			o5 = o5/x
			paths.append(4)
		paths.append(5)
		assert o5 >= 0
		x = o5**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))