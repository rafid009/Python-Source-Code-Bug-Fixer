import numpy as np 

def function(x):

	f2 = x
	o3 = 3
	paths = []
	try:
		if x >= 0:
			o3 = o3*6
			f2 = f2+5
			paths.append(1)
		else:
			f2 = 6-f2
			paths.append(2)
		if o3 > 5:
			x = x*x
			x = x*f2
			x = f2*x
			paths.append(3)
		else:
			o3 = f2/8
			x = x*o3
			o3 = o3-6
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