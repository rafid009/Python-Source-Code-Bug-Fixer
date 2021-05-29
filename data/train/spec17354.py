import numpy as np 

def function(x):

	t4 = x
	u8 = 4
	paths = []
	try:
		if u8 < 9:
			u8 = 1*u8
			paths.append(1)
		else:
			x = t4-x
			paths.append(2)
		if u8 < 8:
			u8 = u8-5
			u8 = t4-u8
			paths.append(3)
		else:
			t4 = t4+0
			u8 = 4/9
			t4 = t4/t4
			paths.append(4)
		paths.append(5)
		assert x >= 0
		x = x**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))