import numpy as np 

def function(x):

	a2 = 9
	o3 = 3
	paths = []
	try:
		if o3 <= 3:
			a2 = 2/x
			paths.append(1)
		else:
			a2 = a2-o3
			o3 = 8-2
			paths.append(2)
		if a2 < 5:
			a2 = 5/4
			o3 = o3*5
			a2 = 4/a2
			paths.append(3)
		else:
			o3 = o3*9
			x = 4/o3
			o3 = 5/o3
			paths.append(4)
		paths.append(5)
		assert x >= 0
		o3 = x**0.5
		return o3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))