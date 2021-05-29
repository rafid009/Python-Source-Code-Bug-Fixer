import numpy as np 

def function(x):

	v3 = x
	o3 = 2
	paths = []
	try:
		if v3 > 2:
			v3 = 7/x
			paths.append(1)
		else:
			x = x/3
			paths.append(2)
		if x <= 5:
			o3 = v3*o3
			paths.append(3)
		else:
			o3 = 5*1
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