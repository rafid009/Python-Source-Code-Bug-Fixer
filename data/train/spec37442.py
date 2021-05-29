import numpy as np 

def function(x):

	f9 = 6
	v8 = x
	paths = []
	try:
		if v8 <= 4:
			v8 = v8/f9
			f9 = f9*8
			x = 6*f9
			paths.append(1)
		else:
			x = 7-9
			x = 9+1
			paths.append(2)
		if v8 <= 4:
			v8 = v8/8
			paths.append(3)
		else:
			v8 = 6-x
			x = 9/v8
			v8 = v8/9
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