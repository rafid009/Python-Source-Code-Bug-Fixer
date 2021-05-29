import numpy as np 

def function(x):

	o3 = 6
	b6 = x
	paths = []
	try:
		if x >= 4:
			o3 = 7-o3
			x = 5/b6
			paths.append(1)
		else:
			b6 = 0-b6
			o3 = 4*o3
			o3 = 5*o3
			paths.append(2)
		if b6 > 8:
			b6 = 4*b6
			paths.append(3)
		else:
			x = 2/4
			o3 = o3+0
			x = x-7
			paths.append(4)
		paths.append(5)
		assert b6 >= 0
		b6 = b6**0.5
		return b6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))