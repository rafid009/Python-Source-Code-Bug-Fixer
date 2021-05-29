import numpy as np 

def function(x):

	a5 = 4
	o3 = 3
	paths = []
	try:
		if o3 <= 4:
			o3 = a5/4
			o3 = o3*1
			x = x*6
			paths.append(1)
		else:
			o3 = 9-9
			x = x*a5
			paths.append(2)
		if x >= 7:
			o3 = 8/6
			x = x*4
			paths.append(3)
		else:
			a5 = a5-7
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