import numpy as np 

def function(x):

	p6 = 0
	u8 = x
	x = x
	paths = []
	try:
		if x >= 4:
			x = 1*1
			p6 = u8*3
			x = 4*8
			paths.append(1)
		else:
			u8 = u8*7
			paths.append(2)
		if x <= 8:
			p6 = p6/7
			x = 0+x
			u8 = 8+u8
			paths.append(3)
		else:
			u8 = 7*u8
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