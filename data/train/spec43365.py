import numpy as np 

def function(x):

	v5 = x
	u8 = 8
	paths = []
	try:
		if v5 > 6:
			v5 = 7+v5
			paths.append(1)
		else:
			u8 = u8/v5
			x = u8-3
			paths.append(2)
		if x < 7:
			v5 = v5-7
			paths.append(3)
		else:
			x = 7+x
			x = x*v5
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