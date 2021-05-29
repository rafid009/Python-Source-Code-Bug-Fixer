import numpy as np 

def function(x):

	b7 = 3
	u8 = 3
	paths = []
	try:
		if b7 > 3:
			x = 6+x
			x = x+0
			paths.append(1)
		else:
			x = x+x
			x = x+8
			b7 = 2+5
			paths.append(2)
		if u8 <= 8:
			u8 = u8+9
			u8 = 7/4
			paths.append(3)
		else:
			x = b7/u8
			u8 = u8/2
			b7 = b7-b7
			paths.append(4)
		paths.append(5)
		assert x >= 0
		b7 = x**0.5
		return b7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))