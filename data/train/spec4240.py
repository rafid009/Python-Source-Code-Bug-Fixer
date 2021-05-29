import numpy as np 

def function(x):

	u8 = 1
	j6 = x
	paths = []
	try:
		if u8 < 6:
			u8 = u8/1
			paths.append(1)
		else:
			x = 8*x
			j6 = 0-u8
			paths.append(2)
		if x >= 8:
			u8 = 1+0
			paths.append(3)
		else:
			x = u8*u8
			j6 = 0*j6
			u8 = u8-3
			paths.append(4)
		paths.append(5)
		assert u8 >= 0
		j6 = u8**0.5
		return j6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))