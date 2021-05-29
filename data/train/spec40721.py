import numpy as np 

def function(x):

	y8 = 9
	v8 = 8
	paths = []
	try:
		if v8 <= 1:
			v8 = v8+5
			paths.append(1)
		else:
			y8 = 7*y8
			y8 = 3/y8
			x = x+x
			paths.append(2)
		if x > 2:
			v8 = x*v8
			y8 = 6-3
			v8 = x/2
			paths.append(3)
		else:
			x = y8/x
			v8 = v8/v8
			v8 = v8+4
			paths.append(4)
		paths.append(5)
		assert x >= 0
		y8 = x**0.5
		return y8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))