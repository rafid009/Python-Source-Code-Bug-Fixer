import numpy as np 

def function(x):

	o3 = 5
	f3 = x
	paths = []
	try:
		if o3 < 8:
			o3 = f3+o3
			paths.append(1)
		else:
			f3 = f3+o3
			o3 = o3/8
			x = x+f3
			paths.append(2)
		if x > 3:
			f3 = 7*f3
			paths.append(3)
		else:
			f3 = 1*7
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