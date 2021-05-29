import numpy as np 

def function(x):

	o3 = x
	n3 = 1
	paths = []
	try:
		if x > 6:
			x = x+8
			n3 = n3+0
			paths.append(1)
		else:
			x = 9+x
			paths.append(2)
		if x >= 1:
			o3 = 1-8
			x = x-x
			o3 = 1/n3
			paths.append(3)
		else:
			o3 = x-o3
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