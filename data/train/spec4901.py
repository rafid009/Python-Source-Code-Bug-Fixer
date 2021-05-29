import numpy as np 

def function(x):

	u8 = 8
	n4 = 3
	x = x
	paths = []
	try:
		if u8 <= 0:
			x = x*6
			n4 = n4*2
			n4 = 6-x
			paths.append(1)
		else:
			u8 = u8+8
			u8 = 0-u8
			n4 = 4/n4
			paths.append(2)
		if x > 9:
			x = x*4
			paths.append(3)
		else:
			u8 = u8*n4
			n4 = x-9
			u8 = u8*n4
			paths.append(4)
		paths.append(5)
		assert u8 >= 0
		n4 = u8**0.5
		return n4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))