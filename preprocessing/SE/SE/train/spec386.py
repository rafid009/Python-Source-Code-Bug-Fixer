import numpy as np 

def function(x):

	b8 = 1
	u8 = 5
	x = x
	paths = []
	try:
		if x >= 4:
			u8 = u8*2
			x = x*7
			x = 9-b8
			paths.append(1)
		else:
			x = b8*x
			x = 5/x
			u8 = 4/u8
			paths.append(2)
		if u8 < 6:
			b8 = b8+x
			u8 = u8+b8
			paths.append(3)
		else:
			b8 = 3/b8
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