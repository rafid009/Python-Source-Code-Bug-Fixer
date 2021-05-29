import numpy as np 

def function(x):

	u8 = 2
	t2 = 6
	paths = []
	try:
		if u8 > 4:
			t2 = 2-t2
			paths.append(1)
		else:
			t2 = t2/7
			t2 = t2*u8
			x = 3*x
			paths.append(2)
		if t2 < 1:
			t2 = 0-1
			paths.append(3)
		else:
			u8 = 3/t2
			u8 = 6/8
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