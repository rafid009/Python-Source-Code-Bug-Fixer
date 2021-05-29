import numpy as np 

def function(x):

	v5 = 6
	o3 = x
	paths = []
	try:
		if o3 > 3:
			v5 = o3+8
			o3 = o3-x
			paths.append(1)
		else:
			o3 = o3*2
			paths.append(2)
		if v5 >= 5:
			x = 8-x
			x = 1-x
			paths.append(3)
		else:
			x = 2/v5
			o3 = 2/9
			x = x/6
			paths.append(4)
		paths.append(5)
		assert x >= 0
		v5 = x**0.5
		return v5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))