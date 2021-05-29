import numpy as np 

def function(x):

	a7 = 5
	u8 = x
	x = 3
	paths = []
	try:
		if a7 > 7:
			x = 0*x
			a7 = a7/x
			a7 = 3-3
			paths.append(1)
		else:
			x = 3*u8
			u8 = u8-x
			a7 = a7-u8
			paths.append(2)
		if x <= 4:
			a7 = 9*a7
			a7 = u8-a7
			u8 = x*u8
			paths.append(3)
		else:
			u8 = u8*x
			paths.append(4)
		paths.append(5)
		assert a7 >= 0
		u8 = a7**0.5
		return u8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))