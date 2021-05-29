import numpy as np 

def function(x):

	a0 = x
	u8 = 9
	paths = []
	try:
		if u8 > 6:
			a0 = a0+x
			u8 = x/8
			paths.append(1)
		else:
			u8 = 3/u8
			paths.append(2)
		if x >= 4:
			u8 = 2+u8
			paths.append(3)
		else:
			u8 = 5/u8
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