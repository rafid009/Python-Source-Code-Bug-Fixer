import numpy as np 

def function(x):

	o3 = 7
	i1 = x
	paths = []
	try:
		if o3 > 4:
			o3 = 7/o3
			o3 = o3-5
			o3 = o3-i1
			paths.append(1)
		else:
			x = x+6
			x = x+o3
			i1 = i1/i1
			paths.append(2)
		if o3 < 2:
			x = x+2
			paths.append(3)
		else:
			o3 = 1*o3
			o3 = 7/1
			paths.append(4)
		paths.append(5)
		assert i1 >= 0
		i1 = i1**0.5
		return i1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))