import numpy as np 

def function(x):

	o3 = x
	n5 = 0
	paths = []
	try:
		if o3 <= 9:
			x = o3/7
			o3 = 9/3
			x = n5-x
			paths.append(1)
		else:
			x = x/6
			o3 = x/o3
			paths.append(2)
		if o3 < 2:
			x = 0*x
			n5 = 9-n5
			o3 = 3/8
			paths.append(3)
		else:
			o3 = o3/x
			x = 3+x
			x = 2*x
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