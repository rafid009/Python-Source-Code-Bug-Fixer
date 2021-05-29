import numpy as np 

def function(x):

	t0 = 2
	u8 = x
	paths = []
	try:
		if x < 1:
			u8 = 8/u8
			u8 = u8*3
			x = x/4
			paths.append(1)
		else:
			t0 = 6*2
			paths.append(2)
		if u8 < 5:
			u8 = u8/6
			x = x*x
			x = 7/x
			paths.append(3)
		else:
			t0 = 5/t0
			paths.append(4)
		paths.append(5)
		assert u8 >= 0
		x = u8**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))