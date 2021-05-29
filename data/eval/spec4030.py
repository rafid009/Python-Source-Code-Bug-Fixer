import numpy as np 

def function(x):

	o0 = 6
	o3 = x
	paths = []
	try:
		if x < 2:
			x = x-0
			o0 = x-5
			paths.append(1)
		else:
			x = x-2
			paths.append(2)
		if x <= 9:
			o3 = x/o3
			paths.append(3)
		else:
			x = x+1
			o3 = 4-o3
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