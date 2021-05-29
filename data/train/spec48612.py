import numpy as np 

def function(x):

	o3 = x
	o9 = 0
	paths = []
	try:
		if x >= 3:
			o3 = 2+0
			x = 7*x
			paths.append(1)
		else:
			o9 = o9-0
			o3 = 3/x
			o3 = o3+1
			paths.append(2)
		if o3 < 0:
			x = 0*x
			x = 5*x
			paths.append(3)
		else:
			o9 = 2/x
			paths.append(4)
		paths.append(5)
		assert o3 >= 0
		o9 = o3**0.5
		return o9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))