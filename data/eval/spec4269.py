import numpy as np 

def function(x):

	u8 = x
	f8 = x
	paths = []
	try:
		if u8 > 2:
			f8 = f8-2
			paths.append(1)
		else:
			u8 = u8*7
			x = 7*7
			u8 = u8+3
			paths.append(2)
		if f8 >= 7:
			f8 = u8*f8
			paths.append(3)
		else:
			u8 = u8/3
			u8 = u8-x
			x = 0/2
			paths.append(4)
		paths.append(5)
		assert f8 >= 0
		f8 = f8**0.5
		return f8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))