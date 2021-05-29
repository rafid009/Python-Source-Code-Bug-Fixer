import numpy as np 

def function(x):

	u8 = 4
	f2 = 2
	paths = []
	try:
		if x <= 0:
			x = 8/u8
			u8 = 0-u8
			paths.append(1)
		else:
			f2 = f2-9
			x = x/2
			paths.append(2)
		if f2 < 6:
			f2 = f2-f2
			f2 = f2/2
			paths.append(3)
		else:
			u8 = 1/4
			u8 = 4*u8
			u8 = 2+4
			paths.append(4)
		paths.append(5)
		assert u8 >= 0
		f2 = u8**0.5
		return f2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))