import numpy as np 

def function(x):

	r5 = x
	u8 = 4
	paths = []
	try:
		if r5 > 0:
			u8 = 3/9
			r5 = r5*4
			paths.append(1)
		else:
			x = x/u8
			paths.append(2)
		if r5 <= 2:
			x = r5+7
			paths.append(3)
		else:
			x = x-5
			paths.append(4)
		paths.append(5)
		assert x >= 0
		u8 = x**0.5
		return u8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))