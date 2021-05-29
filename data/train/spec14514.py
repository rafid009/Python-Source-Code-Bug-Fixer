import numpy as np 

def function(x):

	f5 = x
	o3 = 8
	paths = []
	try:
		if x < 7:
			o3 = o3-5
			x = x-8
			o3 = 0+9
			paths.append(1)
		else:
			f5 = 7/4
			o3 = o3/o3
			paths.append(2)
		if x >= 3:
			o3 = 0/o3
			paths.append(3)
		else:
			o3 = 0+o3
			f5 = f5/f5
			paths.append(4)
		paths.append(5)
		assert x >= 0
		f5 = x**0.5
		return f5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))