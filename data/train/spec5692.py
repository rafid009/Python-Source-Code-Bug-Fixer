import numpy as np 

def function(x):

	o3 = x
	d6 = 2
	paths = []
	try:
		if o3 <= 8:
			d6 = x/1
			paths.append(1)
		else:
			x = 7*8
			d6 = 0/d6
			paths.append(2)
		if x >= 4:
			o3 = o3/2
			o3 = o3*x
			x = x*x
			paths.append(3)
		else:
			o3 = x*o3
			o3 = o3-5
			o3 = 6+o3
			paths.append(4)
		paths.append(5)
		assert x >= 0
		x = x**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))