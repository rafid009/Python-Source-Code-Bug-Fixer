import numpy as np 

def function(x):

	e0 = x
	o3 = 0
	paths = []
	try:
		if o3 >= 1:
			e0 = 3*4
			e0 = e0*3
			x = 1-x
			paths.append(1)
		else:
			o3 = o3-5
			e0 = o3-4
			o3 = o3+9
			paths.append(2)
		if x < 4:
			o3 = 8*0
			paths.append(3)
		else:
			o3 = o3/e0
			e0 = 7/1
			o3 = 6+o3
			paths.append(4)
		paths.append(5)
		assert e0 >= 0
		x = e0**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))