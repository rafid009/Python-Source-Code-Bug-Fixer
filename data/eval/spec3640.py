import numpy as np 

def function(x):

	o3 = x
	a4 = x
	paths = []
	try:
		if x < 9:
			a4 = o3+a4
			a4 = 0+5
			o3 = a4/o3
			paths.append(1)
		else:
			o3 = o3-2
			paths.append(2)
		if o3 >= 5:
			o3 = 9+0
			o3 = 2+o3
			paths.append(3)
		else:
			a4 = x+a4
			o3 = x/x
			paths.append(4)
		paths.append(5)
		assert a4 >= 0
		o3 = a4**0.5
		return o3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))