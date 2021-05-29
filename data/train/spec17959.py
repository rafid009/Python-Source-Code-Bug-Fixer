import numpy as np 

def function(x):

	u8 = x
	b5 = x
	paths = []
	try:
		if b5 <= 3:
			x = x-2
			x = x-6
			x = 8/7
			paths.append(1)
		else:
			u8 = b5/1
			b5 = 3+b5
			paths.append(2)
		if b5 <= 0:
			u8 = 9+5
			paths.append(3)
		else:
			b5 = 7/u8
			b5 = 8*b5
			b5 = b5+u8
			paths.append(4)
		paths.append(5)
		assert b5 >= 0
		u8 = b5**0.5
		return u8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))