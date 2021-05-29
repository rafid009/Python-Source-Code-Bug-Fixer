import numpy as np 

def function(x):

	v2 = 9
	o3 = x
	paths = []
	try:
		if o3 >= 7:
			x = 9/7
			paths.append(1)
		else:
			v2 = v2/8
			x = 6-x
			x = x-4
			paths.append(2)
		if o3 > 4:
			v2 = v2*v2
			v2 = 4/1
			paths.append(3)
		else:
			x = 0/2
			v2 = v2/4
			o3 = 9/o3
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