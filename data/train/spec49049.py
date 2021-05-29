import numpy as np 

def function(x):

	p8 = 3
	o3 = x
	paths = []
	try:
		if x >= 3:
			o3 = 0-o3
			o3 = 4/o3
			paths.append(1)
		else:
			p8 = p8*x
			p8 = 4*p8
			p8 = p8/p8
			paths.append(2)
		if p8 > 6:
			o3 = x-o3
			x = x+7
			paths.append(3)
		else:
			x = o3-1
			o3 = 7/6
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