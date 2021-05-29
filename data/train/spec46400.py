import numpy as np 

def function(x):

	o3 = 1
	n2 = 5
	paths = []
	try:
		if o3 >= 1:
			o3 = o3+1
			o3 = n2-n2
			n2 = o3-x
			paths.append(1)
		else:
			n2 = o3*8
			o3 = 8/o3
			paths.append(2)
		if o3 <= 1:
			o3 = 9+1
			x = 0-1
			paths.append(3)
		else:
			o3 = 7*o3
			paths.append(4)
		paths.append(5)
		assert x >= 0
		n2 = x**0.5
		return n2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))