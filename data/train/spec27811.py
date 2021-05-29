import numpy as np 

def function(x):

	v0 = 8
	o3 = x
	paths = []
	try:
		if o3 < 4:
			v0 = 1-x
			x = 9*x
			x = o3*v0
			paths.append(1)
		else:
			o3 = o3*o3
			o3 = v0/9
			x = o3-4
			paths.append(2)
		if v0 <= 2:
			x = 8-2
			x = v0*9
			paths.append(3)
		else:
			o3 = o3*4
			v0 = v0-x
			paths.append(4)
		paths.append(5)
		assert v0 >= 0
		x = v0**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))