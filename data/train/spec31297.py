import numpy as np 

def function(x):

	f4 = x
	u8 = x
	paths = []
	try:
		if u8 > 2:
			f4 = f4+9
			u8 = u8*0
			f4 = 4+f4
			paths.append(1)
		else:
			x = x+7
			u8 = u8+8
			u8 = u8-u8
			paths.append(2)
		if u8 >= 4:
			x = x*3
			paths.append(3)
		else:
			u8 = 1-5
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