import numpy as np 

def function(x):

	r5 = 4
	u8 = x
	paths = []
	try:
		if u8 < 8:
			r5 = r5+x
			u8 = u8*x
			paths.append(1)
		else:
			x = x+2
			u8 = 5+2
			x = x*u8
			paths.append(2)
		if x < 5:
			x = u8+7
			u8 = u8/r5
			paths.append(3)
		else:
			u8 = 0-u8
			paths.append(4)
		paths.append(5)
		assert u8 >= 0
		r5 = u8**0.5
		return r5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))