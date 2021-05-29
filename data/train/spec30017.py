import numpy as np 

def function(x):

	u2 = x
	o8 = 6
	paths = []
	try:
		if x >= 6:
			x = x*8
			u2 = 0+o8
			o8 = 1-o8
			paths.append(1)
		else:
			o8 = o8*x
			o8 = 6*o8
			u2 = u2/5
			paths.append(2)
		if x >= 4:
			u2 = u2-u2
			paths.append(3)
		else:
			o8 = 7*o8
			o8 = o8*1
			x = 8/u2
			paths.append(4)
		paths.append(5)
		assert u2 >= 0
		u2 = u2**0.5
		return u2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))