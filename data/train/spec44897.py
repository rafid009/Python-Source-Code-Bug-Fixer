import numpy as np 

def function(x):

	p9 = x
	o3 = 4
	paths = []
	try:
		if p9 < 2:
			p9 = p9-1
			o3 = o3+9
			paths.append(1)
		else:
			o3 = 6-5
			paths.append(2)
		if o3 < 8:
			o3 = 0*p9
			x = 0-x
			paths.append(3)
		else:
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