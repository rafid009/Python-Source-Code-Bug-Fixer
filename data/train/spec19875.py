import numpy as np 

def function(x):

	q8 = x
	v0 = x
	paths = []
	try:
		if v0 > 1:
			v0 = v0-x
			q8 = x/q8
			v0 = 8/6
			paths.append(1)
		else:
			q8 = 6-v0
			v0 = 1-3
			v0 = 3/4
			paths.append(2)
		if x < 8:
			v0 = v0+0
			paths.append(3)
		else:
			q8 = 1/q8
			x = q8+x
			x = 8*1
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