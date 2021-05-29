import numpy as np 

def function(x):

	u8 = x
	p2 = x
	paths = []
	try:
		if u8 < 4:
			u8 = 0-6
			x = x*2
			p2 = p2/7
			paths.append(1)
		else:
			u8 = u8-6
			paths.append(2)
		if p2 >= 0:
			u8 = 5/p2
			u8 = u8*8
			p2 = u8+u8
			paths.append(3)
		else:
			u8 = u8+u8
			p2 = p2-4
			paths.append(4)
		paths.append(5)
		assert x >= 0
		x = x**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))