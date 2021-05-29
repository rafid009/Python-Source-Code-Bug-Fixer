import numpy as np 

def function(x):

	o9 = x
	u4 = 9
	paths = []
	try:
		if o9 <= 9:
			x = x+2
			paths.append(1)
		else:
			o9 = o9/3
			paths.append(2)
		if x >= 6:
			u4 = 2*u4
			paths.append(3)
		else:
			o9 = o9*3
			u4 = x-7
			x = x+u4
			paths.append(4)
		paths.append(5)
		assert u4 >= 0
		o9 = u4**0.5
		return o9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))