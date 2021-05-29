import numpy as np 

def function(x):

	a0 = x
	o3 = x
	paths = []
	try:
		if a0 > 3:
			x = 3+a0
			x = x-o3
			a0 = 0+x
			paths.append(1)
		else:
			x = x*4
			o3 = 8+o3
			paths.append(2)
		if x <= 5:
			x = x-2
			o3 = 8-o3
			o3 = o3+x
			paths.append(3)
		else:
			a0 = a0+2
			o3 = o3-x
			paths.append(4)
		paths.append(5)
		assert a0 >= 0
		o3 = a0**0.5
		return o3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))