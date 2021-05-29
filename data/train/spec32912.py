import numpy as np 

def function(x):

	u8 = 6
	b3 = x
	paths = []
	try:
		if b3 > 8:
			b3 = 6/b3
			x = x*3
			u8 = 7+7
			paths.append(1)
		else:
			u8 = u8+9
			x = u8-b3
			u8 = 1-u8
			paths.append(2)
		if u8 >= 3:
			u8 = u8+x
			paths.append(3)
		else:
			x = x-4
			paths.append(4)
		paths.append(5)
		assert b3 >= 0
		b3 = b3**0.5
		return b3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))