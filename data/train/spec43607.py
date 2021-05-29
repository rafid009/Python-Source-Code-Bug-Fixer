import numpy as np 

def function(x):

	r1 = x
	u8 = 4
	paths = []
	try:
		if u8 < 1:
			r1 = r1/u8
			paths.append(1)
		else:
			u8 = r1*1
			r1 = r1-9
			paths.append(2)
		if x < 9:
			u8 = u8/1
			paths.append(3)
		else:
			u8 = x/u8
			u8 = 1/u8
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