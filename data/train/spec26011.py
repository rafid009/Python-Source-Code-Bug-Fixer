import numpy as np 

def function(x):

	b4 = 1
	o3 = x
	paths = []
	try:
		if o3 < 3:
			x = 6+x
			x = 6/x
			x = 9+x
			paths.append(1)
		else:
			x = x/8
			b4 = b4+3
			o3 = o3*9
			paths.append(2)
		if o3 > 6:
			x = x-9
			x = x+7
			paths.append(3)
		else:
			x = x-b4
			o3 = 4+o3
			paths.append(4)
		paths.append(5)
		assert x >= 0
		b4 = x**0.5
		return b4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))