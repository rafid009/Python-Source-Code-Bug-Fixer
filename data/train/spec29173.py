import numpy as np 

def function(x):

	n1 = 2
	o3 = x
	paths = []
	try:
		if o3 < 8:
			x = x+9
			n1 = 5-n1
			paths.append(1)
		else:
			o3 = 0/x
			paths.append(2)
		if x >= 0:
			x = o3+0
			n1 = n1+6
			paths.append(3)
		else:
			o3 = 0-o3
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