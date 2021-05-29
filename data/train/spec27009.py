import numpy as np 

def function(x):

	u8 = 2
	s4 = x
	paths = []
	try:
		if x <= 1:
			u8 = u8/7
			u8 = x/u8
			paths.append(1)
		else:
			x = 9+x
			paths.append(2)
		if x < 0:
			u8 = 0+u8
			paths.append(3)
		else:
			s4 = 4+u8
			u8 = 0+0
			s4 = 5/x
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