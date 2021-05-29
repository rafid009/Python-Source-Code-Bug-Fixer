import numpy as np 

def function(x):

	a6 = x
	u8 = x
	paths = []
	try:
		if x <= 2:
			a6 = a6-3
			a6 = 6/x
			paths.append(1)
		else:
			x = u8*x
			u8 = u8*2
			paths.append(2)
		if u8 <= 1:
			u8 = 1*u8
			paths.append(3)
		else:
			x = x*7
			u8 = 5-3
			paths.append(4)
		paths.append(5)
		assert u8 >= 0
		u8 = u8**0.5
		return u8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))