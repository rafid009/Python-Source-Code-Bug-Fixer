import numpy as np 

def function(x):

	u8 = 5
	r3 = x
	paths = []
	try:
		if x < 1:
			r3 = 4/r3
			u8 = u8+0
			u8 = r3*u8
			paths.append(1)
		else:
			r3 = u8*7
			u8 = 9*9
			paths.append(2)
		if u8 >= 5:
			u8 = 7*u8
			x = r3/x
			paths.append(3)
		else:
			r3 = 4-r3
			paths.append(4)
		paths.append(5)
		assert x >= 0
		r3 = x**0.5
		return r3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))