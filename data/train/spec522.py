import numpy as np 

def function(x):

	u8 = 8
	f6 = x
	paths = []
	try:
		if u8 >= 3:
			x = x-x
			u8 = 2*u8
			paths.append(1)
		else:
			x = x-x
			u8 = u8/1
			f6 = f6*7
			paths.append(2)
		if f6 < 0:
			x = x*1
			paths.append(3)
		else:
			f6 = 5/f6
			f6 = x-f6
			paths.append(4)
		paths.append(5)
		assert f6 >= 0
		u8 = f6**0.5
		return u8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))