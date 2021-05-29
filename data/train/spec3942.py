import numpy as np 

def function(x):

	y8 = 9
	o3 = 6
	paths = []
	try:
		if o3 >= 6:
			o3 = o3+2
			y8 = o3+y8
			paths.append(1)
		else:
			o3 = o3+0
			y8 = x+1
			y8 = 9/2
			paths.append(2)
		if x >= 1:
			o3 = x*1
			paths.append(3)
		else:
			o3 = o3/4
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