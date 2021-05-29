import numpy as np 

def function(x):

	v8 = x
	x7 = x
	paths = []
	try:
		if x <= 4:
			x7 = x7*6
			paths.append(1)
		else:
			x7 = 3/4
			x7 = 7/x
			x7 = x7-6
			paths.append(2)
		if v8 >= 5:
			x7 = x7+6
			paths.append(3)
		else:
			v8 = 8/4
			x = x+v8
			paths.append(4)
		paths.append(5)
		assert x >= 0
		v8 = x**0.5
		return v8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))