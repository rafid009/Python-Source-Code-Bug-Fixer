import numpy as np 

def function(x):

	t0 = x
	u8 = 2
	paths = []
	try:
		if u8 >= 6:
			u8 = x-t0
			u8 = 4*u8
			paths.append(1)
		else:
			t0 = t0*1
			paths.append(2)
		if u8 > 6:
			t0 = t0-3
			x = 3*t0
			t0 = t0*9
			paths.append(3)
		else:
			x = x+6
			u8 = x/t0
			paths.append(4)
		paths.append(5)
		assert t0 >= 0
		u8 = t0**0.5
		return u8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))