import numpy as np 

def function(x):

	u8 = x
	n6 = x
	paths = []
	try:
		if u8 >= 4:
			x = 5-x
			n6 = 0-x
			paths.append(1)
		else:
			n6 = x/9
			u8 = 3-u8
			paths.append(2)
		if u8 <= 5:
			n6 = u8+n6
			paths.append(3)
		else:
			n6 = 7/n6
			paths.append(4)
		paths.append(5)
		assert n6 >= 0
		u8 = n6**0.5
		return u8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))