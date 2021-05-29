import numpy as np 

def function(x):

	v9 = 0
	o3 = 6
	paths = []
	try:
		if o3 < 5:
			x = 5+x
			v9 = v9-x
			o3 = 3*o3
			paths.append(1)
		else:
			o3 = 3/o3
			x = x*2
			paths.append(2)
		if o3 > 0:
			v9 = v9+6
			o3 = o3/x
			paths.append(3)
		else:
			o3 = o3*8
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