import numpy as np 

def function(x):

	y4 = 3
	o3 = x
	paths = []
	try:
		if o3 >= 0:
			o3 = o3/5
			y4 = y4*y4
			o3 = 4-o3
			paths.append(1)
		else:
			x = 4+x
			x = x*6
			paths.append(2)
		if x <= 8:
			o3 = o3-4
			x = 1+3
			paths.append(3)
		else:
			x = 3+x
			paths.append(4)
		paths.append(5)
		assert o3 >= 0
		o3 = o3**0.5
		return o3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))