import numpy as np 

def function(x):

	x9 = 6
	v8 = 6
	paths = []
	try:
		if x < 2:
			x9 = 7*v8
			paths.append(1)
		else:
			x9 = 2/v8
			v8 = v8+x9
			paths.append(2)
		if x9 <= 0:
			v8 = v8+8
			x9 = 0-x9
			v8 = 0/v8
			paths.append(3)
		else:
			x = 5+x
			x = x/4
			v8 = v8+8
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