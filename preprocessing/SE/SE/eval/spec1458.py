import numpy as np 

def function(x):

	v2 = 9
	o3 = 1
	paths = []
	try:
		if o3 <= 3:
			v2 = x*v2
			paths.append(1)
		else:
			x = x*6
			x = v2/x
			paths.append(2)
		if v2 <= 6:
			o3 = v2+4
			x = v2+8
			x = 4+x
			paths.append(3)
		else:
			o3 = 3+o3
			x = 0/v2
			paths.append(4)
		paths.append(5)
		assert o3 >= 0
		v2 = o3**0.5
		return v2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))