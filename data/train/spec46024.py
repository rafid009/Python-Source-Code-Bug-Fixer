import numpy as np 

def function(x):

	u8 = 9
	r7 = 4
	x = x
	paths = []
	try:
		if x < 5:
			r7 = 4-r7
			paths.append(1)
		else:
			u8 = u8*5
			x = x*r7
			paths.append(2)
		if x > 8:
			u8 = 4*u8
			paths.append(3)
		else:
			r7 = 4*x
			paths.append(4)
		paths.append(5)
		assert x >= 0
		x = x**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))