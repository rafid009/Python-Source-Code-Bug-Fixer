import numpy as np 

def function(x):

	v0 = 6
	u8 = 4
	paths = []
	try:
		if v0 > 9:
			u8 = u8-v0
			x = 7*x
			paths.append(1)
		else:
			u8 = u8+x
			paths.append(2)
		if u8 < 2:
			v0 = v0+6
			paths.append(3)
		else:
			x = 0*x
			v0 = v0+9
			u8 = 5+u8
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