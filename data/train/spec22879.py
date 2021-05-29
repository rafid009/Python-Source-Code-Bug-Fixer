import numpy as np 

def function(x):

	o3 = 0
	n8 = 3
	paths = []
	try:
		if n8 < 8:
			o3 = 8-n8
			paths.append(1)
		else:
			x = x*o3
			paths.append(2)
		if x >= 4:
			n8 = x+o3
			paths.append(3)
		else:
			o3 = 6+o3
			n8 = 1+x
			paths.append(4)
		paths.append(5)
		assert n8 >= 0
		o3 = n8**0.5
		return o3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))