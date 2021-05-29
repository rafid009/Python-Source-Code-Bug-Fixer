import numpy as np 

def function(x):

	o3 = x
	d5 = 8
	paths = []
	try:
		if x <= 0:
			d5 = 0+d5
			paths.append(1)
		else:
			d5 = d5/8
			paths.append(2)
		if d5 >= 2:
			d5 = d5*8
			d5 = 7-d5
			x = 9-8
			paths.append(3)
		else:
			o3 = x-7
			d5 = 9+d5
			paths.append(4)
		paths.append(5)
		assert o3 >= 0
		o3 = o3**0.5
		return o3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))