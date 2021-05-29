import numpy as np 

def function(x):

	u8 = x
	q8 = x
	paths = []
	try:
		if q8 < 6:
			x = 9+x
			u8 = u8/4
			q8 = q8+5
			paths.append(1)
		else:
			x = x+u8
			x = 3-1
			q8 = u8+q8
			paths.append(2)
		if x <= 9:
			x = x*q8
			paths.append(3)
		else:
			x = u8+u8
			x = x-0
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