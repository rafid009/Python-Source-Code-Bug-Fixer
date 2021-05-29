import numpy as np 

def function(x):

	y5 = x
	o3 = x
	paths = []
	try:
		if o3 >= 2:
			o3 = 1*2
			x = 7*y5
			paths.append(1)
		else:
			y5 = 7-9
			o3 = 8*x
			paths.append(2)
		if y5 >= 5:
			x = x*x
			x = x-1
			y5 = 8/5
			paths.append(3)
		else:
			x = 5-4
			o3 = o3/6
			paths.append(4)
		paths.append(5)
		assert o3 >= 0
		x = o3**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))