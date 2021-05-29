import numpy as np 

def function(x):

	e3 = 8
	u8 = 7
	paths = []
	try:
		if u8 > 9:
			e3 = e3-0
			paths.append(1)
		else:
			x = x/7
			paths.append(2)
		if x < 8:
			e3 = e3*e3
			e3 = x+2
			x = 9/u8
			paths.append(3)
		else:
			u8 = 8*u8
			e3 = u8-e3
			paths.append(4)
		paths.append(5)
		assert e3 >= 0
		u8 = e3**0.5
		return u8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))