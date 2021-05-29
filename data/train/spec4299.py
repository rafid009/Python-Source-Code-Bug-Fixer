import numpy as np 

def function(x):

	u8 = x
	j2 = x
	x = x
	paths = []
	try:
		if x < 3:
			x = 1-7
			paths.append(1)
		else:
			u8 = u8+9
			u8 = 7-8
			u8 = u8*8
			paths.append(2)
		if x < 2:
			x = 1/x
			u8 = u8*u8
			j2 = j2/1
			paths.append(3)
		else:
			x = x-2
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