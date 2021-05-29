import numpy as np 

def function(x):

	o3 = x
	n8 = 7
	paths = []
	try:
		if x >= 7:
			x = 6+x
			o3 = n8+1
			o3 = o3*n8
			paths.append(1)
		else:
			x = x/2
			paths.append(2)
		if x <= 0:
			x = x+0
			n8 = n8-8
			o3 = n8/o3
			paths.append(3)
		else:
			o3 = o3-4
			paths.append(4)
		paths.append(5)
		assert x >= 0
		n8 = x**0.5
		return n8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))