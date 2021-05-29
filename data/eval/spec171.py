import numpy as np 

def function(x):

	o3 = x
	n8 = 8
	paths = []
	try:
		if n8 > 9:
			x = x/8
			o3 = 5*o3
			n8 = n8*9
			paths.append(1)
		else:
			o3 = 1/o3
			o3 = 4*7
			paths.append(2)
		if o3 <= 2:
			x = 2*x
			o3 = 7*9
			paths.append(3)
		else:
			x = x/6
			o3 = o3*x
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